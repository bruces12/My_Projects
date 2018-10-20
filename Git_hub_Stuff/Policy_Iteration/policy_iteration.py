# policy_iteration.py
"""Volume 2: Policy Function Iteration.
<Name>
<Class>
<Date>
"""

import numpy as np
from scipy import linalg as la
import time
from matplotlib import pyplot as plt


def value_iteration(V_0, beta=.9, N=500, W_max=1, u=np.sqrt, tol=1e-6,
                    max_iter=500):
    """Perform VI according to the Bellman optimality principle

    Parameters:
        V_0 (ndarray) - The initial guess for the value function
        beta (float) - The discount rate (between 0 and 1)
        N (int) - The number of pieces you will split the cake into
        W_max (float) - The value of W_max
        u (function) - The utility function (u(0) = 0; u' > 0; u'' < 0; and lim_{c->0+} u'(c) = \inf)
        tol (float) - The stopping criteria for the value iteration
        max_iter (int) - An alternative stopping criteria

    Returns:
        V_final (ndarray) - The discrete values for the true value function (Problem 1)
        c (list) - The amount of cake to consume at each time to maximize utility (Problem 3)
    """
    N=N+1
    w=np.linspace(0,W_max,N)#discretize the space
    for i in range(max_iter):#iterate up to as much as maxiter
        V_P1=np.zeros(N)
        for i in range(N):
            V_P1[i]=np.max(u(w[i]-w[:i+1])+beta*V_0[:i+1])
        if la.norm(V_0-V_P1)<tol:#if within our tolerance, we can break
            break
        V_0=np.copy(V_P1)
    policy=np.zeros(N)
    for i in range(N):#define our policy
        policy[i]=np.argmax(u(w[i]-w[:i+1])+beta*V_P1[:i+1])
    return V_P1,extract_policy_vector(w,policy)

def extract_policy_vector(possible_W, policy_function):
    """Returns the policy vector that determines how much cake should be eaten at each time step

    Parameters:
        possible_W (ndarray) - an array representing the discrete values of W
        policy_function (ndarray) - an array representing how many pieces to leave at each state

    Returns:
        c (list) - a list representing how much cake to eat at each time period
    """
    c=[]
    w=np.max(possible_W)
    count=0
    next=1
    while sum(c)<np.max(possible_W):
        index=np.argmin(abs(possible_W-w))#find how much is left and get that index
        next=w-possible_W[int(policy_function[index])]
        if next!=0:#if we aren't adding zero pieces append, else break
            c.append(next)
        else:
            break
        w-=next
        count+=1
    return c

def policy_iteration(pi_0, beta=.9, N=500, W_max=1, u=np.sqrt, max_iter=50):
    """Perform PI according to the Bellman optimality principle

    Parameters:
        pi_0 (array) - The initial guess for the Policy Function (0 <= pi_0(W) <= W)
        beta (float) - The discount rate (between 0 and 1)
        N (int) - The number of pieces you will split the cake into
            also acts as a cap for the number of steps required to calculate V_k at each iteration
        W_max (float) - The value of W_max
        u (function) - The utility function (u(0) = 0; u' > 0; u'' < 0; and lim_{c->0+} u'(c) = \inf)
        max_iter (int) - An alternative stopping criteria for the policy function updates

    Returns:
        V_final (ndarray) - The discrete values for the true value function
        c (list) - The amount of cake to consume at each time to maximize utility
    """
    N+=1
    w=np.linspace(0,W_max,N)#discretize w
    pi_0=pi_0.astype('int')#make sure pi_0 can be used as indices
    for i in range(max_iter):
        values=[0]
        pi_1=[0]
        for j in range(1,len(w)):
            values.append(u(w[j]
            -w[pi_0[j]])
            +beta*values[pi_0[j]])
        values=np.array(values)
        for k in range(1,len(w)):
            pi_1.append(np.argmax(u(w[k]-w[:k+1])+beta*values[:k+1]))
        if la.norm(pi_0-pi_1,np.inf)<.1:#we let tol be .1 because pi has indices in it, so any deviation will result in an error of at least one, so .1 is more than small enough
            break
        pi_0=np.array(pi_1)
    return values,extract_policy_vector(w,pi_1)

def compare_methods():
    """
    Solve the cake eating problem with each method, VI, PI with various values of beta and compare how long each method takes.
    Each V_final should be np.allclose and each policy vector, c, should be identical for each both.
    Use N=1000 as the number of grid points for w and beta = [.95, .975, .99, .995].

    Graph the results for each method with beta on the x-axis and time on the y-axis.
    """
    polit=[]
    valit=[]
    pi=np.zeros(1001)
    pi[1:]=np.arange(1000)#define our initial guesses
    v0=np.sqrt(np.linspace(0,1,1001))
    betas=np.array([.95,.975,.99,.995])#initialize the betas
    for i in betas:#time each beta
        start=time.time()
        v,c=policy_iteration(pi,beta=i,N=1000)
        polit.append(time.time()-start)
        start=time.time()
        v,c=value_iteration(v0,beta=i,N=1000)
        valit.append(time.time()-start)
    plt.plot(betas,np.array(polit),'-b')#plot the data
    plt.plot(betas,np.array(valit),'-r')
    plt.legend(('PI Time','VI Time'))
    plt.xlabel('Beta')
    plt.ylabel('Time (Seconds)')
    plt.title('Policy vs. Value Iteration')
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

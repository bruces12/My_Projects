
import numpy as np
from scipy import sparse
from scipy import linalg as la

def to_matrix(filename, n,delim=None):
    """Return the nxn adjacency matrix described by datafile.

    Parameters:
        datafile (str): The name of a .txt file describing a directed graph.
        Lines describing edges should have the form '<from node>\t<to node>\n'.
        The file may also include comments.
    n (int): The number of nodes in the graph described by datafile

    Returns:
        A SciPy sparse dok_matrix.
    """
    with open(filename) as file:#open the file
        mat=file.readlines()
    mats=[]
    for i in mat:#iterate through the values form the file
        try:
            mats.append(i.strip().split(delim))#separate according to tab
        except:
            None
    adj_mat=sparse.dok_matrix((n,n))
    for i in mats:
        try:
            adj_mat[int(i[0]),int(i[1])]=1#get the first and second values and they correspond to row and column
        except:
            None
    return adj_mat#return the adjacency matrix


def calculateK(A,N):
    """Compute the matrix K as described in the lab.

    Parameters:
        A (ndarray): adjacency matrix of an array
        N (int): the datasize of the array

    Returns:
        K (ndarray)
    """
    D=np.sum(A,axis=1)#find D as a vector
    mask=D==0#find zero rows
    D[mask]=N
    A[mask]=1
    return (np.diag(1/D) @ A).T #return k


def iter_solve(adj, N=None, d=.85, tol=1E-5):
    """Return the page ranks of the network described by 'adj'.
    Iterate through the PageRank algorithm until the error is less than 'tol'.

    Parameters:
        adj (ndarray): The adjacency matrix of a directed graph.
        N (int): Restrict the computation to the first 'N' nodes of the graph.
            If N is None (default), use the entire matrix.
        d (float): The damping factor, a float between 0 and 1.
        tol (float): Stop iterating when the change in approximations to the
            solution is less than 'tol'.

    Returns:
        The approximation to the steady state.
    """
    if N is not None:
        adj=adj[N,N]
    k=calculateK(adj,len(adj))#find k
    p=np.random.random(len(k))#initialize our guess for p
    dif=np.inf
    while dif>tol:#iterate until we are within the desired tolerance
        p1=d*k @ p+((1-d)/len(k))
        dif=la.norm(p1-p)
        p=p1
    return p#return final guess


def eig_solve(adj, N=None, d=.85):
    """Return the page ranks of the network described by 'adj'. Use SciPy's
    eigenvalue solver to calculate the steady state of the PageRank algorithm

    Parameters:
        adj (ndarray): The adjacency matrix of a directed graph.
        N (int): Restrict the computation to the first 'N' nodes of the graph.
            If N is None (default), use the entire matrix.
        d (float): The damping factor, a float between 0 and 1.
        tol (float): Stop iterating when the change in approximations to the
            solution is less than 'tol'.

    Returns:
        The approximation to the steady state.
    """
    if N is not None:
        adj=adj[:N,:N]#adjust the part we are working with
    k=calculateK(adj,len(adj))#find k
    B=d*k+(1-d)/len(k)#find B
    eigs=la.eig(B)#calculate values and vectors
    one=np.argmax(eigs[0])#find largest
    rankse = eigs[1][:,one]
    return rankse/np.sum(rankse)#return normalized corresponding vector


def team_rank(filename='ncaa2013.csv'):
    """Use iter_solve() to predict the rankings of the teams in the given
    dataset of games. The dataset should have two columns, representing
    winning and losing teams. Each row represents a game, with the winner on
    the left, loser on the right. Parse this data to create the adjacency
    matrix, and feed this into the solver to predict the team ranks.

    Parameters:
        filename (str): The name of the data file.
    Returns:
        ranks (list): The ranks of the teams from best to worst.
        teams (list): The names of the teams, also from best to worst.
    """
    with open(filename) as file:
        data=file.readlines()[1:]
    dta=[]
    for i in data:
        dta.append(i.strip().split(','))
    dtap=np.array(dta).ravel()
    teams=[]
    for i in dtap:
        if i not in teams:
            teams.append(i)
    team_dict={}
    for i in range(len(teams)):
        team_dict[teams[i]]=i
    adj_matrix=sparse.dok_matrix((len(teams),len(teams)))
    for i in dta:
        adj_matrix[team_dict[i[1]],team_dict[i[0]]]=1
    ranks=iter_solve(adj_matrix.toarray(),d=.7)
    rank_copy=np.copy(ranks)
    ranked_list=[]
    for i in range(len(teams)):
        index=np.argmax(rank_copy)
        ranked_list.append(teams[index])
        teams.remove(teams[index])
        rank_copy=np.delete(rank_copy,index)
    return np.sort(ranks)[len(ranks)::-1],ranked_list
        
        
        
        
        
        
        
        
        
    


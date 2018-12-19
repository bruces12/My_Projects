import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation


def ai_turn(c1,c2):
    pows=np.array([i.power for i in np.array(c1.master_map.regions)[c1.bords]])
    targ1=c1.bords[np.argmin(pows)]
    for i in c1.master_map.neighbs[targ1]:
        if i in c1.regions:
            source=i
            break
    c1.attack(targ1,source,.2)
    pows=np.array([i.power for i in np.array(c2.master_map.regions)[c2.bords]])
    targ2=c2.bords[np.argmin(pows)]
    for i in c2.master_map.neighbs[targ2]:
       if i in c2.regions:
            source=i
            break
    c2.attack(targ2,source,.6)
    c1.resupply(.9,.18)
    c2.resupply(.9,.2)
    return np.copy(c1.master_map.array)
    
def ani(c1,c2,length=60):
    """
    animates a map of random battles between two ai opponents
    note that c2 has the advantage in this simulation
    parameters:
        c1: class country, first country in the war
        c2: class country, second country in the war
        length, int number of iterations to keep the war goind for
    """
    fig = plt.figure()
    
    ims = []
    for i in range(length):
        x=ai_turn(c1, c2).astype(float)
        im = plt.imshow(x, animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True,
                                    repeat_delay=1000)

    plt.show()

def get_neighbors(index, radius, height, width):
    """Calculate the flattened indices of the pixels that are within the given
    distance of a central pixel, and their distances from the central pixel.

    Parameters:
        index (int): The index of a central pixel in a flattened image array
            with original shape (radius, height).
        radius (float): Radius of the neighborhood around the central pixel.
        height (int): The height of the original image in pixels.
        width (int): The width of the original image in pixels.

    Returns:
        (1-D ndarray): the indices of the pixels that are within the specified
            radius of the central pixel, with respect to the flattened image.
        (1-D ndarray): the euclidean distances from the neighborhood pixels to
            the central pixel.
    """
    # Calculate the original 2-D coordinates of the central pixel.
    row, col = index // width, index % width

    # Get a grid of possible candidates that are close to the central pixel.
    r = int(radius)
    x = np.arange(max(col - r, 0), min(col + r + 1, width))
    y = np.arange(max(row - r, 0), min(row + r + 1, height))
    X, Y = np.meshgrid(x, y)

    # Determine which candidates are within the given radius of the pixel.
    R = np.sqrt(((X - col)**2 + (Y - row)**2))
    mask = R < radius
    return (X[mask] + Y[mask]*width).astype(np.int), R[mask]

class region:
    #a class to keep track of a small portion of the big map
    #countries are made up of a collection of regions
    def __init__(self,land_coors,power,color,type,shape):
        """
        parameters:
            cap:boolean, is this the capital, will be used in later updates
            land_coors:[list-ints], list of the indices of the pixels making up the region in the flattended map
            power: float, the power of the region, higher is harder to conquer
            color, nd-array (,3) the rgb value of the color that will be displayed on the map
            type: string wither land or sea, only land tiles can be invaded
            shape: tuple shape of the full map
        """
        self.land=land_coors
        bord=[]
        for i in land_coors:
            bord+=[j for j in get_neighbors(i,1.1,shape[0],shape[1])[0] if j not in land_coors]
        self.bords=bord
        self.power=power
        self.color=color
        self.power=power
        self.type=type
        self.owner=None
        
        
    
class country:
    #class defining a nation
    def __init__(self,regions,master_map,color,cap):
        """
        parameters:
            regions, [list-ints] a list of indices corresponding to the regions list for the master-map
            master_map, class map-the map object that this country belongs to
            color, nd-array (,3) the rgb value of the color that will be displayed on the map
        """
        self.master_map=master_map
        self.regions=regions
        self.cap=cap
        self.master_map.regions[cap].power*=5
        self.color=color
        bords=[]
        for i in regions:
            master_map.update_color(color,i)
            bords+=[j for j in master_map.neighbs[i] if j not in regions and j not in bords]
        self.bords=bords
        for i in regions:
            self.master_map.regions[i].owner=self
        
    def attack(self,target,source,power_portion):
        """
        adds functionality so a country can attack a neighboring region
        parameters:
            target, int-the index of the region being attacked
            source, int-the index of the region attacking the target
            power_portion, float (0,1), portion of the power from source being used to attack
        """
        power=self.master_map.regions[source].power*power_portion
        if self.master_map.regions[target].type=='land' and target in self.bords:
            res=self.battle(self.master_map.regions[target],power)
            if res>0:
                for i in self.master_map.regions[target].land:
                    self.master_map.array[i//self.master_map.shape[1],i%self.master_map.shape[1],:]=self.master_map.regions[target].color
                self.regions+=[target]
                self.master_map.regions[target].power=min(power,res)
                self.master_map.regions[source].power=self.master_map.regions[source].power-power
                self.master_map.update_color(self.color,target)
                defender=self.master_map.regions[target].owner
                if defender:
                    defender.regions.remove(target)
                    defender.update_borders()
                self.master_map.regions[target].owner=self
                self.bords+=[j for j in self.master_map.neighbs[target] if j not in self.regions and j not in self.bords]
            else:
                self.master_map.regions[target].power=min(self.master_map.regions[target].power,-res)
                self.master_map.regions[source].power=self.master_map.regions[source].power-power
        else:
            raise ValueError('Target is untargetable, either it is not a border, or it is a sea tile')
        
    def resupply(self,factor,cap_add):
        """
        function to resupply regions belonging to the country
        """
        add_factor=(1-factor)/4.6
        for i in self.regions:
            self.master_map.regions[i].power*=factor
            for j in self.master_map.neighbs[i]:
                self.master_map.regions[j].power+=self.master_map.regions[i].power*add_factor
        self.master_map.regions[self.cap].power+=cap_add
    
    def battle(self,target,power):
        """
        determines the winn of invasions
        there will be more functionality added as the simulator has new features added
        parameters:
            target, int the index of invaded region corresponding to the list form the master map
            power, float- the power of the invading forces
        """
        return np.random.randn()+power-target.power
        
    def update_borders(self):
        """
        updates borders after a successful invasion
        """
        bords=[]
        for i in self.regions:
            bords+=[j for j in self.master_map.neighbs[i] if j not in self.regions and j not in bords]
        self.bords=bords
                
        
        
            
            
class map_:
    def __init__(self,regions,shape,neighbs):
        """
        map class:
            parameters:
                regions-a list of objects of type region, all the regions contained in the map,
                shape- tuple (n,m,3) with n and m ints
                neighbs- dict, keys are indices for the regions list, maps to a list of indices that are the neighbors of the region at the key location
            attributes:
                shape-(tuple (n,m,3) with n and m ints)
                array-
        """
        self.shape=shape
        
        self.array=np.zeros(shape)
        self.regions=regions
        for i in regions:
            for j in i.land:
                self.array[j//shape[1],j%shape[1],:]=i.color
        self.neighbs=neighbs
        
    def update_color(self,color,index):
        """
        updates colors of regions as needed
        color, nd-array (,3) the rgb value of the new color that will be displayed on the map
        index, int index of the region being updated
        """
        self.regions[index].color=color
        for j in self.regions[index].land:
            self.array[j//self.shape[1],j%self.shape[1],:]=self.regions[index].color
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
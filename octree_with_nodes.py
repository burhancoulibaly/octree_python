import math

class OctreeNode:
    count = 0
    totPoints = 0
    lowestDist = 255
    lowestDistPoint = None
    emptyQuad = False
    

    def __init__(self,object):
        self.root = object
        self.q1 = None
        self.q2 = None
        self.q3 = None
        self.q4 = None
        self.q5 = None
        self.q6 = None
        self.q7 = None
        self.q8 = None
    
    def setQ1(self,object):
        self.q1 = (object)
    def setQ2(self,object):
        self.q2 = (object)
    def setQ3(self,object):
        self.q3 = (object)
    def setQ4(self,object):
        self.q4 = (object)
    def setQ5(self,object):
        self.q5 = (object)
    def setQ6(self,object):
        self.q6 = (object)
    def setQ7(self,object):
        self.q7 = (object)
    def setQ8(self,object):
        self.q8 = (object)
    
    def getChildren(self,root):
        return [root.getQ1(),root.getQ2(),root.getQ3(),root.getQ4(),root.getQ5(),root.getQ6(),root.getQ7(),root.getQ8()]

    def getQ1(self):
        return self.q1
    def getQ2(self):
        return self.q2
    def getQ3(self):
        return self.q3
    def getQ4(self):
        return self.q4
    def getQ5(self):
        return self.q5
    def getQ6(self):
        return self.q6
    def getQ7(self):
        return self.q7
    def getQ8(self):
        return self.q8

    def getTotalPoints(self,root,count=0):
        if(count == 0):
            OctreeNode.count = 0

        if(root.root.isDivided == False):
            OctreeNode.count += len(root.root.points)
            return OctreeNode.count
        
        octree = self.getChildren(root)

        for node in octree:
            if(node.root.isDivided != True):
                OctreeNode.count += len(node.root.points)
            else:
                self.getTotalPoints(node.root.node,OctreeNode.count)
        return OctreeNode.count

    def closestImageRGB(self,root,point):
        self.quadPoints = 0

        if(root.root.isDivided == False):
            print("corresponding quad found")
            for point2 in node.root.points:
                print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                    OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                    OctreeNode.lowestDistPoint = point2
                else:
                    continue
                    
        octree = self.getChildren(root)
        for i,node in enumerate(octree):
            if(OctreeNode.emptyQuad == True):
                print("previous quad was empty")
                if(len(node.root.points) != 0):
                    if(node.root.isDivided != True):
                        if(len(node.root.points) == 0):
                            print("quad was empty finding closest point amoungst neighboring quads")
                            itrs = 0
                            if(i-1 > 0 and i+1 <= 8):
                                while(i-1 > 0 and i+1 <= 8):
                                    print("searching from middle")
                                    if(len(octree[i-itrs].root.points) != 0 or len(octree[i+itrs].root.points) != 0):
                                        OctreeNode.emptyQuad = False
                                        mergedPoints = octree[i-1].root.points + octree[i+1].root.points
                                        for point2 in mergedPoints:
                                            print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                                            if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                                                OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                                                OctreeNode.lowestDistPoint = point2
                                            else:
                                                continue
                                    else:
                                        continue
                            elif(i-1 < 0):
                                while(i+1 <= 8):
                                    print("searching from end")
                                    if(len(octree[i+itrs].root.points) != 0):
                                        OctreeNode.emptyQuad = False
                                        for point2 in octree[i+itrs].root.points:
                                            print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                                            if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                                                OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                                                OctreeNode.lowestDistPoint = point2
                                            else:
                                                continue
                            else:
                                while(i-1 > 0):
                                    print("searching from beginning")
                                    if(len(octree[i-itrs].root.points) != 0):
                                        OctreeNode.emptyQuad = False
                                        for point2 in octree[i-itrs].root.points:
                                            print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                                            if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                                                OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                                                OctreeNode.lowestDistPoint = point2
                                            else:
                                                continue
                        else:
                            print("corresponding quad found(After Empty Node)")
                            OctreeNode.emptyQuad = False
                            for point2 in node.root.points:
                                print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                                if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                                    OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                                    OctreeNode.lowestDistPoint = point2
                                else:
                                    continue
                            break
                    else:
                        # print("changing nested quad")
                        self.closestImageRGB(node.root.node, point)
                else:
                    OctreeNode.emptyQuad = True
                    print("This parent node is empty")
                    OctreeNode.emptyQuad = True
                    if(i+1 > 8):
                        while(i > 0):
                            self.closestImageRGB(octree[i-1],point)
                    else:
                        continue


            if(node.root.boundary.contains(point) == True):
                if(len(node.root.points) != 0):
                    if(node.root.isDivided != True):
                        if(len(node.root.points) == 0):
                            print("quad was empty finding closest point amoungst neighboring quads")
                            itrs = 0
                            if(i-1 > 0 and i+1 <= 8):
                                while(i-1 > 0 and i+1 <= 8):
                                    print("searching from middle")
                                    if(len(octree[i-itrs].root.points) != 0 or len(octree[i+itrs].root.points) != 0):
                                        mergedPoints = octree[i-1].root.points + octree[i+1].root.points
                                        for point2 in mergedPoints:
                                            print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                                            if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                                                OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                                                OctreeNode.lowestDistPoint = point2
                                            else:
                                                continue
                                    else:
                                        continue
                            elif(i-1 < 0):
                                while(i+1 <= 8):
                                    print("searching from end")
                                    if(len(octree[i+itrs].root.points) != 0):
                                        for point2 in octree[i+itrs].root.points:
                                            print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                                            if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                                                OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                                                OctreeNode.lowestDistPoint = point2
                                            else:
                                                continue
                            else:
                                while(i-1 > 0):
                                    print("searching from beginning")
                                    if(len(octree[i-itrs].root.points) != 0):
                                        for point2 in octree[i-itrs].root.points:
                                            print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                                            if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                                                OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                                                OctreeNode.lowestDistPoint = point2
                                            else:
                                                continue
                        else:
                            print("corresponding quad found")
                            for point2 in node.root.points:
                                print(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)),point2.x,point2.y,point2.z)
                                if(math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2)) < OctreeNode.lowestDist):
                                    OctreeNode.lowestDist = math.sqrt(((point.x-point2.x)**2)+((point.y-point2.y)**2)+((point.y-point2.y)**2))
                                    OctreeNode.lowestDistPoint = point2
                                else:
                                    continue
                            break
                    else:
                        # print("changing nested quad")
                        self.closestImageRGB(node.root.node, point)
                else:
                    print("This parent node is empty")
                    OctreeNode.emptyQuad = True
                    if(i+1 > 8):
                        while(i > 0):
                            self.closestImageRGB(octree[i-1],point)
                    else:
                        continue
    
            else:
                continue
        OctreeNode.lowestDist = 255
        return OctreeNode.lowestDistPoint

class Rectangle:
    def __init__(self,x,y,z,w,h):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.divCount = 0
        

    def contains(self,point):
        # print(self.x - self.w,">=",point.x,"<=",self.x + self.w)
        # print(self.y - self.w,">=",point.y,"<=",self.y + self.w)
        # print(self.z - self.h,">=", point.z,"<=",self.z + self.h)
        # print(point.x >= self.x - self.w and point.x <= self.x + self.w and point.y >= self.y - self.w and point.y <= self.y + self.w and point.z >= self.z - self.h and point.z <= self.z + self.h)
        return(point.x >= self.x - self.w and point.x <= self.x + self.w and point.y >= self.y - self.w and point.y <= self.y + self.w and point.z >= self.z - self.h and point.z <= self.z + self.h)

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        

class Octree:   
    def __init__(self,boundary,capacity):
       self.points = []
       self.boundary = boundary
       self.capacity = capacity
       self.isDivided = False
       self.node = OctreeNode(self)

    def newPoint(self,point):
        if(self.node.root.boundary.contains(point) != True):
            # print("not contained")
            return False

        if(len(self.node.root.points) < self.node.root.capacity):
            # print("point added", point.x, point.y, point.z)
            self.node.root.points.append(point)
            return True
        else:
            if(self.node.root.isDivided != True):
                # print("Max capacity reached in this quadrant")
                # print("this quad has been divided")   
                self.node.root.subDivide()

            if(self.node.q1.root.newPoint(point)):
                return True
            elif(self.node.q2.root.newPoint(point)):
                return True
            elif(self.node.q3.root.newPoint(point)):
                return True
            elif(self.node.q4.root.newPoint(point)):
                return True
            elif(self.node.q5.root.newPoint(point)):
                return True
            elif(self.node.q6.root.newPoint(point)):
                return True
            elif(self.node.q7.root.newPoint(point)):
                return True
            elif(self.node.q8.root.newPoint(point)):
                return True
    
    def subDivide(self):
        x = self.node.root.boundary.x
        y = self.node.root.boundary.y
        z = self.node.root.boundary.z
        w = self.node.root.boundary.w
        h = self.node.root.boundary.h

        q1 = Rectangle(x + w/2,y+w/2,z+h/2,w/2,h/2)
        self.node.setQ1(OctreeNode(Octree(q1,self.capacity)))
        q2 = Rectangle(x - w/2,y+w/2,z+h/2,w/2,h/2)
        self.node.setQ2(OctreeNode(Octree(q2,self.capacity)))
        q3 = Rectangle(x + w/2,y+h/2,z-w/2,w/2,h/2)
        self.node.setQ3(OctreeNode(Octree(q3,self.capacity)))
        q4 = Rectangle(x - w/2,y+h/2,z-w/2,w/2,h/2)
        self.node.setQ4(OctreeNode(Octree(q4,self.capacity)))

        q5 = Rectangle(x + w/2,y-w/2,z+h/2,w/2,h/2)
        self.node.setQ5(OctreeNode(Octree(q5,self.capacity)))
        q6 = Rectangle(x - w/2,y-w/2,z+h/2,w/2,h/2)
        self.node.setQ6(OctreeNode(Octree(q6,self.capacity)))
        q7 = Rectangle(x + w/2,y-h/2,z-w/2,w/2,h/2)
        self.node.setQ7(OctreeNode(Octree(q7,self.capacity)))
        q8 = Rectangle(x - w/2,y-h/2,z-w/2,w/2,h/2)
        self.node.setQ8(OctreeNode(Octree(q8,self.capacity)))

        for point in self.node.root.points:
            # print("point redistribution")
            if(self.node.q1.root.boundary.contains(point) == True):
                self.node.q1.root.points.append(point)
                # print("point redistributed to quad1")
            elif(self.node.q2.root.boundary.contains(point) == True):
                self.node.q2.root.points.append(point)
                # print("point redistributed to quad2")
            elif(self.node.q3.root.boundary.contains(point) == True):
                self.node.q3.root.points.append(point)
                # print("point redistributed to quad3")
            elif(self.node.q4.root.boundary.contains(point) == True):
                self.node.q4.root.points.append(point)
                # print("point redistributed to quad4")
            elif(self.node.q5.root.boundary.contains(point) == True):
                self.node.q5.root.points.append(point)
                # print("point redistributed to quad5")
            elif(self.node.q6.root.boundary.contains(point) == True):
                self.node.q6.root.points.append(point)
                # print("point redistributed to quad6")
            elif(self.node.q7.root.boundary.contains(point) == True):
                self.node.q7.root.points.append(point)
                # print("point redistributed to quad7")
            elif(self.node.q8.root.boundary.contains(point) == True):
                self.node.q8.root.points.append(point)
                # print("point redistributed to quad8")
            else:
                print("You've made a grave mistake this point goes in none of the quads")


        self.node.root.isDivided = True
        self.node.root.boundary.divCount += 1



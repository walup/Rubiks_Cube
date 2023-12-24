#Today i thought about implementing a Rubiks cube, which is another puzzle i like

from enum import Enum
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D

#Let's start by simply defining the colors of the piece faces
class PieceColor(Enum):
    NEUTRAL = [31/255, 27/255, 27/255]
    ORANGE = [237/255, 98/255, 33/255]
    BLUE = [0/255, 63/255, 237/255]
    GREEN = [44/255, 145/255, 0/255]
    RED = [204/255, 20/255, 42/255]
    WHITE = [245/255, 245/255, 245/255]
    YELLOW = [247/255, 192/255, 25/255]

class CubeFace(Enum):
    FRONT = "F"
    BACK = "B"
    RIGHT = "R"
    LEFT = "L"
    UP = "U"
    DOWN = "D"
    
class Axis(Enum):
    X = 0
    Y = 1
    Z = 2
    
#Now let's define our pieces. 
class Piece:
    
    #front, back, left, right, top, down, are sort of arbitrary. But we will choose a system of reference where the blue face of the cube is 
    #the front face, and the yellow face is the top face. 
    
    def __init__(self, frontColor, backColor, leftColor, rightColor, topColor, downColor, xPos, yPos, zPos, width, height, depth):
        self.frontColor = frontColor
        self.backColor = backColor
        self.leftColor = leftColor
        self.rightColor = rightColor
        self.topColor = topColor
        self.downColor = downColor

        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.width = width
        self.height = height
        self.depth = depth
    
    def rotateFaces(self, axis, counter):
        if(axis == Axis.Y and not counter):
            bottomColor = self.rightColor
            topColor = self.leftColor
            rightColor = self.topColor
            leftColor = self.downColor
            
            self.downColor = bottomColor
            self.topColor = topColor
            self.rightColor = rightColor
            self.leftColor = leftColor
        
        elif(axis == Axis.Y and counter):
            bottomColor = self.leftColor
            topColor = self.rightColor
            rightColor = self.downColor
            leftColor = self.topColor
            
            self.downColor = bottomColor
            self.topColor = topColor
            self.rightColor = rightColor
            self.leftColor = leftColor
            
        
        elif(axis == Axis.X and not counter):
            topColor = self.frontColor
            downColor = self.backColor
            frontColor = self.downColor
            backColor = self.topColor
            
            self.topColor = topColor
            self.downColor = downColor
            self.frontColor = frontColor
            self.backColor = backColor
        
        elif(axis == Axis.X and counter):
            topColor = self.backColor
            downColor = self.frontColor
            frontColor = self.topColor
            backColor = self.downColor
            
            self.topColor = topColor
            self.downColor = downColor
            self.frontColor = frontColor
            self.backColor = backColor
        
        elif(axis == Axis.Z and not counter):
            rightColor = self.backColor
            leftColor = self.frontColor
            backColor = self.leftColor
            frontColor = self.rightColor
            
            self.rightColor = rightColor
            self.leftColor = leftColor
            self.frontColor = frontColor
            self.backColor = backColor
            
        elif(axis == Axis.Z and counter):
            rightColor = self.frontColor
            leftColor = self.backColor
            backColor = self.rightColor
            frontColor = self.leftColor
            
            self.rightColor = rightColor
            self.leftColor = leftColor
            self.frontColor = frontColor
            self.backColor = backColor
            
            
        
    
    def drawPiece(self, ax):
        #Front face
        x = [self.xPos,self.xPos,self.xPos+self.width,self.xPos+self.width]
        y = [self.yPos,self.yPos,self.yPos,self.yPos]
        z = [self.zPos,self.zPos + self.height,self.zPos+self.height,self.zPos]
        verts = [list(zip(x,y,z))]
        ax.add_collection3d(Poly3DCollection(verts,facecolors = self.frontColor.value))
        
        #back face
        x = [self.xPos,self.xPos,self.xPos+self.width,self.xPos+self.width]
        y = [self.yPos+self.depth,self.yPos+self.depth,self.yPos+self.depth,self.yPos+self.depth]
        z = [self.zPos,self.zPos + self.height,self.zPos+self.height,self.zPos]
        verts = [list(zip(x,y,z))]
        ax.add_collection3d(Poly3DCollection(verts,facecolors = self.backColor.value))
        
        #left face
        x = [self.xPos,self.xPos,self.xPos,self.xPos]
        y = [self.yPos,self.yPos,self.yPos+self.depth,self.yPos+self.depth]
        z = [self.zPos,self.zPos + self.height,self.zPos+self.height,self.zPos]
        verts = [list(zip(x,y,z))]
        ax.add_collection3d(Poly3DCollection(verts,facecolors = self.leftColor.value))
        
        #right face
        x = [self.xPos+self.width,self.xPos+self.width,self.xPos+self.width,self.xPos+self.width]
        y = [self.yPos,self.yPos,self.yPos+self.depth,self.yPos+self.depth]
        z = [self.zPos,self.zPos + self.height,self.zPos+self.height,self.zPos]
        verts = [list(zip(x,y,z))]
        ax.add_collection3d(Poly3DCollection(verts,facecolors = self.rightColor.value))
        
        #bottom face 
        x = [self.xPos,self.xPos+self.width,self.xPos+self.width,self.xPos]
        y = [self.yPos,self.yPos,self.yPos+self.depth,self.yPos+self.depth]
        z = [self.zPos,self.zPos,self.zPos,self.zPos]
        verts = [list(zip(x,y,z))]
        ax.add_collection3d(Poly3DCollection(verts,facecolors = self.downColor.value))
        
        #top face 
        x = [self.xPos,self.xPos+self.width,self.xPos+self.width,self.xPos]
        y = [self.yPos,self.yPos,self.yPos+self.depth,self.yPos+self.depth]
        z = [self.zPos+self.height,self.zPos+self.height,self.zPos+self.height,self.zPos+self.height]
        verts = [list(zip(x,y,z))]
        ax.add_collection3d(Poly3DCollection(verts,facecolors = self.topColor.value))
    

    
class RubiksCube:
    
    def __init__(self):
        
        self.initializeCube()
    
    #Let's create our cube
    def initializeCube(self):
        self.pieces = []
        #Blue face
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.WHITE,0,0,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.WHITE,1,0,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.NEUTRAL, PieceColor.WHITE,2,0,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL,0,0,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL,1,0,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.NEUTRAL, PieceColor.NEUTRAL,2,0,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.YELLOW, PieceColor.NEUTRAL,0,0,2,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.YELLOW, PieceColor.NEUTRAL,1,0,2,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.BLUE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.YELLOW, PieceColor.NEUTRAL,2,0,2,1,1,1)
        self.pieces.append(piece)
        
        #Red face
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.NEUTRAL, PieceColor.WHITE,2,1,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.NEUTRAL, PieceColor.NEUTRAL,2,1,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.YELLOW, PieceColor.NEUTRAL,2,1,2,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.NEUTRAL, PieceColor.WHITE,2,2,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.NEUTRAL, PieceColor.NEUTRAL,2,2,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.NEUTRAL, PieceColor.RED, PieceColor.YELLOW, PieceColor.NEUTRAL,2,2,2,1,1,1)
        self.pieces.append(piece)
        
        #Green face
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.WHITE,1,2,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL,1,2,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.YELLOW, PieceColor.NEUTRAL,1,2,2,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.WHITE,0,2,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL,0,2,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.GREEN, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.YELLOW, PieceColor.NEUTRAL,0,2,2,1,1,1)
        self.pieces.append(piece)
        
        #Orange face
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.WHITE,0,1,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL,0,1,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.ORANGE, PieceColor.NEUTRAL, PieceColor.YELLOW, PieceColor.NEUTRAL,0,1,2,1,1,1)
        self.pieces.append(piece)
        
        #yellow face
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.WHITE,1,1,0,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL,1,1,1,1,1,1)
        self.pieces.append(piece)
        piece = Piece(PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.NEUTRAL, PieceColor.YELLOW, PieceColor.NEUTRAL,1,1,2,1,1,1)
        self.pieces.append(piece)
        
    
    def makeMove(self, moveString):
        counter = False
        if("'" in moveString):
            counter = True
            moveString = moveString.replace("'","")
        
        repetitions = 1
        if(len(moveString) == 2):
            repetitions = int(moveString[1])
            moveString = moveString[0]
        

        if(moveString == CubeFace.FRONT.value):
            self.rotateFrontFace(repetitions, counter)
        elif(moveString == CubeFace.RIGHT.value):
            self.rotateWholeCube(1,False, Axis.Z)
            self.rotateFrontFace(repetitions, counter)
            self.rotateWholeCube(1,True,Axis.Z)
        elif(moveString == CubeFace.LEFT.value):
            self.rotateWholeCube(1,True, Axis.Z)
            self.rotateFrontFace(repetitions, counter)
            self.rotateWholeCube(1,False,Axis.Z)
        elif(moveString == CubeFace.UP.value):
            self.rotateWholeCube(1,True, Axis.X)
            self.rotateFrontFace(repetitions, counter)
            self.rotateWholeCube(1,False,Axis.X)
        elif(moveString == CubeFace.DOWN.value):
            self.rotateWholeCube(1,False, Axis.X)
            self.rotateFrontFace(repetitions, counter)
            self.rotateWholeCube(1,True,Axis.X)
        elif(moveString == CubeFace.BACK.value):
            self.rotateWholeCube(2,False, Axis.Z)
            self.rotateFrontFace(repetitions, counter)
            self.rotateWholeCube(2,True,Axis.Z)
        
            
            
            

            
    def getPieceAtPosition(self, x, y, z):
        threshold = 0.01
        for i in range(0,len(self.pieces)):
            piece = self.pieces[i]
            dst = np.sqrt((piece.xPos - x)**2 + (piece.yPos - y)**2 + (piece.zPos - z)**2)
            if(dst < threshold):
                return piece
        
        return -1
    
    def getFace(self, faceType):
        if(faceType == CubeFace.FRONT):
            xPiecePos = [0,1,2,0,1,2,0,1,2]
            yPiecePos = [0,0,0,0,0,0,0,0,0]
            zPiecePos = [0,0,0,1,1,1,2,2,2]
            
            pieces = []
            
            for i in range(0,len(xPiecePos)):
                piece = self.getPieceAtPosition(xPiecePos[i],yPiecePos[i],zPiecePos[i])
                if(piece == -1):
                    print("Problem at "+str(xPiecePos[i]) + ", "+str(yPiecePos[i]) + ", "+str(zPiecePos[i]))
                pieces.append(piece)
            
            return pieces
        
        elif(faceType == CubeFace.BACK):
            xPiecePos = [0,1,2,0,1,2,0,1,2]
            yPiecePos = [2,2,2,2,2,2,2,2,2]
            zPiecePos = [0,0,0,1,1,1,2,2,2]
            
            pieces = []
            
            for i in range(0,len(xPiecePos)):
                piece = self.getPieceAtPosition(xPiecePos[i],yPiecePos[i],zPiecePos[i])
                pieces.append(piece)
            
            return pieces
        
        elif(faceType == CubeFace.RIGHT):
            xPiecePos = [2,2,2,2,2,2,2,2,2]
            yPiecePos = [0,1,2,0,1,2,0,1,2]
            zPiecePos = [0,0,0,1,1,1,2,2,2]
            
            pieces = []
            
            for i in range(0,len(xPiecePos)):
                piece = self.getPieceAtPosition(xPiecePos[i],yPiecePos[i],zPiecePos[i])
                pieces.append(piece)
            
            return pieces
        
        elif(faceType == CubeFace.LEFT):
            xPiecePos = [0,0,0,0,0,0,0,0,0]
            yPiecePos = [0,1,2,0,1,2,0,1,2]
            zPiecePos = [0,0,0,1,1,1,2,2,2]
            
            pieces = []
            
            for i in range(0,len(xPiecePos)):
                piece = self.getPieceAtPosition(xPiecePos[i],yPiecePos[i],zPiecePos[i])
                pieces.append(piece)
            
            return pieces
            
        
        elif(faceType == CubeFace.UP):
            xPiecePos = [0,1,2,0,1,2,0,1,2]
            yPiecePos = [0,0,0,1,1,1,2,2,2]
            zPiecePos = [2,2,2,2,2,2,2,2,2]
            
            pieces = []
            
            for i in range(0,len(xPiecePos)):
                piece = self.getPieceAtPosition(xPiecePos[i],yPiecePos[i],zPiecePos[i])
                pieces.append(piece)
            
            return pieces
        
        elif(faceType == CubeFace.DOWN):
            xPiecePos = [0,1,2,0,1,2,0,1,2]
            yPiecePos = [0,0,0,1,1,1,2,2,2]
            zPiecePos = [0,0,0,0,0,0,0,0,0]
            
            pieces = []
            
            for i in range(0,len(xPiecePos)):
                piece = self.getPieceAtPosition(xPiecePos[i],yPiecePos[i],zPiecePos[i])
                pieces.append(piece)
            
            return pieces
        
        return -1
    
    def rotateFrontFace(self, turns, counterClockwise):
        angle = 90*(np.pi/180)
        if(counterClockwise):
            angle = -angle
        
        frontPieces = self.getFace(CubeFace.FRONT)
        rotationMatrix = np.array([[np.cos(angle), 0, np.sin(angle)],[0,1,0],[-np.sin(angle), 0, np.cos(angle)]])
        
        midVector = np.array([1,1,1])

        for i in range(0,len(frontPieces)):
            piece = frontPieces[i]
            for j in range(0,turns):
                positionVector = midVector + rotationMatrix.dot(np.array([piece.xPos, piece.yPos, piece.zPos])-midVector)
                piece.xPos = positionVector[0]
                piece.yPos = positionVector[1]
                piece.zPos = positionVector[2]
                
                piece.rotateFaces(Axis.Y, counterClockwise)
        
        
        
        
    
    #A function that rotates the whole cube around any of three axis.
    def rotateWholeCube(self,turns, counterClockwise, axis):
        rotationMatrix = -1
        angle = 90*(np.pi/180)
        if(counterClockwise == False and not axis == Axis.Y):
                angle = -angle
        elif(axis == Axis.Y and counterClockwise):
            angle = -angle
            
        if(axis == Axis.X):
            rotationMatrix = np.array([[1,0,0],[0,np.cos(angle),-np.sin(angle)],[0,np.sin(angle),np.cos(angle)]])
        elif(axis == Axis.Y):
            rotationMatrix = np.array([[np.cos(angle), 0, np.sin(angle)],[0,1,0],[-np.sin(angle), 0, np.cos(angle)]])
                
        elif(axis == Axis.Z):
            rotationMatrix = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle),0],[0,0,1]])
        
        midVector = np.array([1,1,1])

        
        for i in range(0,len(self.pieces)):
            piece = self.pieces[i]
            for j in range(0,turns):
                positionVector = midVector + rotationMatrix.dot(np.array([piece.xPos, piece.yPos, piece.zPos])-midVector)
                piece.xPos = positionVector[0]
                piece.yPos = positionVector[1]
                piece.zPos = positionVector[2]
                
                piece.rotateFaces(axis, counterClockwise)
        
    
    def drawCube(self, azimAngle, elevAngle, rollAngle):
        fig = plt.figure();
        ax = fig.add_subplot(111,projection='3d');
        x, y, z = np.indices((3, 3, 3))
        
        cube = (x >= 0)&(x <= 2) & (y <= 2) & (z <= 2)
        voxelarray = cube
        colors = np.empty(voxelarray.shape, dtype=object)
        colors[cube] = "r"
        ax.voxels(voxelarray,edgecolor='k', facecolors = colors, alpha = 0, linewidth = 2)
        
        for i in range(0,len(self.pieces)):
            piece = self.pieces[i]
            piece.drawPiece(ax)
        
        
        ax.set_xlim([0,3])
        ax.set_ylim([0,3])
        ax.set_zlim([0,3])
        
        ax.view_init(azim=azimAngle, elev=elevAngle, roll = rollAngle)

        ax.set_axis_off()
        
        
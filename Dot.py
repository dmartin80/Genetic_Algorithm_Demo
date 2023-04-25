#imports
from tkinter import *
import Brain
import Direction_Vector as DV
import math
import Canvas_Vars

class dot:
  def __init__(self):
    self.dead = False
    self.reached_goal = False
    self.pos = DV.vector(Canvas_Vars.canvas_width/2, Canvas_Vars.canvas_height-50)
    self.vel = DV.vector(0, 0)
    self.acc = DV.vector(0, 0)
    self.dot_rad = 2
    self.dot_coords = [self.pos.x, self.pos.y, self.pos.x+2*self.dot_rad, self.pos.y+2*self.dot_rad]
    self.dot_object = None
    self.brain = Brain.brain()
    self.fitness = 0
    self.color = "black"

  def updatePosition(self):
    self.acc = self.brain.directions[self.brain.brain_step]
    self.brain.brain_step += 1
    self.vel.add(self.acc)
    self.vel.limit(3)
    self.pos.add(self.vel)
    self.dot_coords = [self.pos.x, self.pos.y, self.pos.x+2*self.dot_rad, self.pos.y+2*self.dot_rad]

  def calculate_fitness(self):
    if self.reached_goal:
      self.fitness = 1.0/16.0 + 10000.0/(math.pow(self.brain.brain_step, 2))
    else:
      dot_centerpoint =  DV.vector(self.pos.x, self.pos.y)
      dot_centerpoint.centerpoint(self.dot_rad)
      distanceToGoal = dot_centerpoint.distance(Canvas_Vars.goal_centerpoint, self.dot_rad, Canvas_Vars.goal_rad)
      self.fitness = 1.0/(math.pow(distanceToGoal, 2))

  def clone_brain(self, parent):
    self.brain.clone(parent)
  
  def set_best_dot(self):
    self.color = "green1"
    


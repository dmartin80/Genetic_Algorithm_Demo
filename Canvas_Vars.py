import Direction_Vector as DV

canvas_width = 500
canvas_height = 500
canvas_border = 30
sudo_border = 3
goal_rad = 5
goal_pos = DV.vector((canvas_width)/2, 0 + canvas_border)
goal_coords = [goal_pos.x, goal_pos.y, goal_pos.x + 2*goal_rad, goal_pos.y + 2*goal_rad]
goal_centerpoint =  DV.vector(goal_pos.x,goal_pos.y)
goal_centerpoint.centerpoint(goal_rad)
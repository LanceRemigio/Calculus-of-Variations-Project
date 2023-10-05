import numpy as np


def x1_el (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    delt_x = x1 - x2
    delt_y = y1 - y2
    list_terms = [ 
                    (c1 * delt_x) / sum((delt_x) ** 2, (delt_y) ** 2 ) ** 2,      

                    (c2 *  (x1 - 2)) / (np.sqrt(x1 - obs1_pos[0])) ** 2, 

                    (y1 - obs1_pos[1] ** 2 - obs1_radius) ** 3 
                    / np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1] ** 2 ))
                ]
    return -list_terms[0] - list_terms[1] + list_terms[2]     

def y1_el (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    delt_x = x1 - x2
    delt_y = y1 - y2
    list_terms = [ 
                    (c1 * delt_y) / sum((delt_x) ** 2, (delt_y) ** 2 ) ** 2,      

                    (c2 *  (y1 - 2)) / (np.sqrt(x1 - obs1_pos[0])) ** 2, 

                    (y1 - obs1_pos[1] ** 2 - obs1_radius) ** 3 
                    / np.sqrt((x1 - obs1_pos[0]) ** 2 + (y1 - obs1_pos[1] ** 2 ))
                ]
    return -list_terms[0] - list_terms[1] + list_terms[2]


def x2_el (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    delt_x = x1 - x2
    delt_y = y1 - y2
    list_terms = [ 
                    (c1 * delt_x) / sum((delt_x) ** 2, (delt_y) ** 2 ) ** 2,      

                    (c2 *  (x2 - 2)) / (np.sqrt(x2 - obs1_pos[0])) ** 2, 

                    (y2 - obs1_pos[1] ** 2 - obs1_radius) ** 3 
                    / np.sqrt((x2 - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1] ** 2 ))
                  ]
    return list_terms[0] - list_terms[1] + list_terms[2]

def y2_el (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    delt_x = x1 - x2
    delt_y = y1 - y2
    list_terms = [ 
                    (c1 * delt_y) / sum((delt_x) ** 2, (delt_y) ** 2 ) ** 2,      

                    (c2 *  (y2 - 2)) / (np.sqrt(x2 - obs1_pos[0])) ** 2, 

                    (y2 - obs1_pos[1] ** 2 - obs1_radius) ** 3 
                    / np.sqrt((x2 - obs1_pos[0]) ** 2 + (y2 - obs1_pos[1] ** 2 ))
                  ]
    return list_terms[0] - list_terms[1] + list_terms[2]


def diff_func (x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius):
    list_func = [ x1_el(x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius), 
                    y1_el(x1,y1, x2, y2, c1, c2, obs1_pos, obs1_radius),   
                ] 
    return list_func[0], list_func[1]



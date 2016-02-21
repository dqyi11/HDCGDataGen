'''
Created on Feb 19, 2016

@author: walter
'''

from xml.dom import minidom
import numpy as np

SPATIAL_RELATIONS = ("in_between", "left_of", "right_of", "top_of", "bottom_of", "avoid" )

class SpatialRelationInfo(object):
    
    def __init__(self):
        self.type = None
        self.obstacles = []
        
    def __str__(self):
        string_label =  str(self.type)+"("
        for i in range(len(self.obstacles)):
            if i >= len(self.obstacles)-1:
                string_label += self.obstacles[i].name
            else:
                string_label += self.obstacles[i].name + ","
        string_label += ")"
        return string_label

class PathPlanningInfo(object):

    def __init__(self, world):
        self.start = None
        self.goal = None
        
        self.world = world
 
        self.segment_length = 5

        self.iteration_num = 5000
        self.costmap_file = ""
        
        self.grammar_type = 0
        self.run_type = 2
        self.min_dist_enabled = 1
        
        self.spatial_relations = []
        
        self.path_output_file = self.world.name
        
    def addCostmapFile(self, costmap_filename):
        if costmap_filename != None:
            self.costmap_file = costmap_filename
            self.min_dist_enabled = 0
        else:
            self.costmap_file = costmap_filename
            self.min_dist_enabled = 1
        
    def randomSpatialRelation(self):
        self.spatial_relations = []
        sr_info = SpatialRelationInfo()
        sr_info.type = np.random.choice(SPATIAL_RELATIONS)
        if sr_info.type == "in_between":
            obs1 = np.random.choice(self.world.obstacles)
            obs2 = np.random.choice(self.world.obstacles)
            while obs1 == obs2:
                obs2 = np.random.choice(self.world.obstacles)
            sr_info.obstacles.append(obs1)
            sr_info.obstacles.append(obs2)
        else:
            obs = np.random.choice(self.world.obstacles)
            sr_info.obstacles.append(obs)
        self.spatial_relations.append(sr_info)
            
        
    def write_to_xml(self, filename):
        
        xmldoc = minidom.Document()
        root = xmldoc.createElement("root")
        xmldoc.appendChild(root)
        
        world_node = xmldoc.createElement("world")
        world_node.setAttribute("map_filename", self.world.filename)
        world_node.setAttribute("map_fullpath", self.world.fullpath)
        world_node.setAttribute("map_width", str(self.world.width))
        world_node.setAttribute("map_height", str(self.world.height))
        world_node.setAttribute("segment_length", str(self.segment_length))
        world_node.setAttribute("max_iteration_num", str(self.iteration_num))
        world_node.setAttribute("grammar_type", str(self.grammar_type))
        world_node.setAttribute("run_type", str(self.run_type))
        world_node.setAttribute("min_dist_enabled", str(self.min_dist_enabled))
        if self.costmap_file == "":
            world_node.setAttribute("objective_file", '')
        else:
            world_node.setAttribute("objective_file", self.costmap_file)
        world_node.setAttribute("path_output_file", self.path_output_file)
        
        world_node.setAttribute("start_x", str(self.world.start[0]))
        world_node.setAttribute("start_y", str(self.world.start[1]))
        world_node.setAttribute("goal_x", str(self.world.goal[0]))
        world_node.setAttribute("goal_y", str(self.world.goal[1]))
        root.appendChild(world_node)
        
        obs_info = xmldoc.createElement("obstacles")
        for obs in self.world.obstacles:
            obs_node = xmldoc.createElement("obstacle")
            obs_node.setAttribute("name", obs.name)
            obs_node.setAttribute("center_x", str(int(obs.centroid[0])))
            obs_node.setAttribute("center_y", str(int(obs.centroid[1])))
            obs_info.appendChild(obs_node)
        world_node.appendChild(obs_info)
        
        spatial_rel_nodes = xmldoc.createElement("spatial_relations")
        for spatial_rel in self.spatial_relations:
            spatial_rel_node = xmldoc.createElement("spatial_relation")
            spatial_rel_node.setAttribute("type", spatial_rel.type)
            for spatial_rel_obs in spatial_rel.obstacles:
                spatial_rel_obs_node = xmldoc.createElement("obs")
                spatial_rel_obs_node.setAttribute("name", spatial_rel_obs.name)
                spatial_rel_node.appendChild(spatial_rel_obs_node)
            spatial_rel_nodes.appendChild(spatial_rel_node)
        world_node.appendChild(spatial_rel_nodes)
        
        xmldoc.writexml( open(filename, 'w'), indent="  ", addindent="  ", newl="\n", encoding='utf-8' )
        xmldoc.unlink()   
        
        
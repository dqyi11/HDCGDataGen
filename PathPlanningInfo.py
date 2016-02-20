'''
Created on Feb 19, 2016

@author: walter
'''

from xml.dom import minidom

SPATIAL_RELATIONS = ("IN_BETWEEN", "LEFT_OF", "RIGHT_OF", "TOP_OF", "BOTTOM_OF", "AVOID" )

class PathPlanningInfo(object):


    def __init__(self, world):
        self.start = None
        self.goal = None
        
        self.world = world
 
        self.segment_length = 5
        self.mapname = ""
        self.mappath = ""
        self.iteration_num = 5000
        self.costmap_file = None
        
        self.grammar_type = 0
        self.run_type = 2
        self.min_dist_enabled = 0
        
    def write_to_xml(self, filename):
        
        xmldoc = minidom.Document()
        root = xmldoc.createElement("world")
        root.setAttribute("map_width", str(self.world.width))
        root.setAttribute("map_height", str(self.world.height))
        root.setAttribute("segment_length", str(self.segment_length))
        root.setAttribute("max_iteration_num", str(self.iteration_num))
        root.setAttribute("grammar_type", str(self.grammar_type))
        root.setAttribute("run_type", str(self.run_type))
        root.setAttribute("min_dist_enabled", str(self.min_dist_enabled))
        root.setAttribute("objective_file",str(self.costmap_file))
        
        obs_info = xmldoc.createElement("obstacles")
        for obs in self.world.obstacles:
            obs_node = xmldoc.createElement("obstacle")
            obs_node.setAttribute("name", obs.name)
            obs_node.setAttribute("center_x", int(obs.centroid[0]))
            obs_node.setAttribute("center_y", int(obs.centroid[1]))
            obs_info.appendChild(obs_node)
        root.appendChild(obs_info)
        
        spatial_rel_nodes = xmldoc.createElement("spatial_relations")
        for spatial_rel in self.spatial_relations:
            spatial_rel_node = xmldoc.createElement("spatial_relation")
            spatial_rel_node.setAttribute("type", spatial_rel.type)
            for spatial_rel_obs in spatial_rel.obstacles:
                spatial_rel_obs_node = xmldoc.createElement("obs")
                spatial_rel_obs_node.setAttribute("name", spatial_rel_obs.name)
                spatial_rel_node.appendChild(spatial_rel_obs_node)
            spatial_rel_nodes.appendChild(spatial_rel_node)
        root.appendChild(spatial_rel_nodes)
        
        
        
        
"""POC for bento_meta"""
import os.path
import sys

import yaml

from bento_mdf.mdf import MDF
from bento_meta.entity import ArgError
from bento_meta.model import Model
from bento_meta.objects import Concept, Node, Property, Tag, Term, ValueSet
from yaml import Loader as yloader

sys.path.insert(0, ".")
sys.path.insert(0, "../src")
sys.path.insert(0, "bento_meta/python")

def create_model():
    m = MDF(handle="test")
    m.files = [
        "./data/c3dc-model.yml",
        "./data/c3dc-model-props.yml",
    ]
    m.load_yaml()
    m.create_model()
    return m

def print_all_node_handles(m):
    for x in m.model.nodes.values():
        print(x.handle)

if __name__ == "__main__":
    m = create_model()
    print_all_node_handles(m)    

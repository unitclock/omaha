# coding: utf-8
from omaha import Omaha
from task import Task

if __name__ == "__main__":
    print("start processing")
    o = Omaha()
    g = o.term_gen()
    print(o.find_synonym_from_concept_id(1000015))

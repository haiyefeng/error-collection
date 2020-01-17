# _*_ coding: utf-8 _*_
__author__ = 'fortune'
__date__ = '2020/1/15 11:10'


def get_children_data(parent_node, children_list):
    children_nodes = parent_node.get_children()
    for index, child in enumerate(children_nodes):
        if child.get_children():
            children_list.append({
                "data": {"text": child.content},
                "children": []
            })
            get_children_data(child, children_list[index].get('children'))
        else:
            children_list.append(
                {"data": {"text": child.content}}
            )

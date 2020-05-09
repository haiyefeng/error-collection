# _*_ coding: utf-8 _*_
__author__ = 'fortune'
__date__ = '2020/1/15 11:10'
import json

from django.db import transaction


# 递归获取子树数据
def get_children_data(parent_node, children_list):
    children_nodes = parent_node.get_children()
    for index, child in enumerate(children_nodes):
        children_list.append({
            "data": {"text": child.content, "id": child.id},
            "children": []
        })
        if child.get_children():
            get_children_data(child, children_list[index].get('children'))


def format_summary_data(summary_list):
    # 获取旧的总结数据实例的id列表，组装新的总结数据，二者对比，增加、删除、更新总结
    from miscollection.models import Summary
    root_data = summary_list.get('root').get('data')
    tree_id = root_data.get('tree_id')
    subject_title = root_data.get('subject_title')
    chapter = root_data.get('chapter')
    old_summarys = Summary.objects.filter(tree_id=tree_id, subject_title=subject_title, chapter=chapter)
    old_id_list = list(old_summarys.values_list('id', flat=True))
    new_dict = {root_data.get('id'): {'content': root_data.get('text'), 'parent': None}}
    if summary_list.get('root').get('children'):
        get_children_list(summary_list.get('root').get('children'), root_data.get('id'), new_dict)
    is_success = edit_summary(old_id_list, new_dict, subject_title, chapter)
    return is_success


def get_children_list(child_list, parent_id, new_data_dict):
    # 递归将子树的信息加入到列表中
    for child_node in child_list:
        data = child_node.get('data')
        new_data_dict.update({data.get('id'): {'content': data.get('text'), 'parent': parent_id}})
        if child_node.get('children'):
            get_children_list(child_node.get('children'), data.get('id'), new_data_dict)


def edit_summary(old_list, new_dict, subject_title, chapter):
    # 根据新旧两个总结的列表长度进行对比，增加、删除或更新总结
    from miscollection.models import Summary
    try:
        with transaction.atomic():
            if len(old_list) > len(new_dict.keys()):
                del_id = list(set(old_list) - set(new_dict.keys()))
                Summary.objects.filter(id__in=del_id).delete()
                del new_dict[del_id]
            for key, summary in new_dict.items():
                obi, created = Summary.objects.update_or_create(
                    defaults={
                        'subject_title': subject_title,
                        'chapter': chapter,
                        'content': summary.get('content'),
                        'parent_id': summary.get('parent'),
                    },
                    id=key,
                )
            return True
    except Exception as e:
        print(e)
        return False

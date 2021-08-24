# https://codeforces.com/problemset/problem/545/C
import sys
from anytree import Node


def build_tree_ds(trees: list) -> Node:
    if trees is None or len(trees) <= 0:
        return None
    tree_ds: Node = Node([-sys.maxsize, -sys.maxsize, 0])
    parent_nodes: list = [tree_ds]
    for i in range(len(trees)):
        left_cut_x = trees[i][0] - trees[i][1]
        right_cut_x = trees[i][0] + trees[i][1]

        current_nodes: list = []
        for parent_node in parent_nodes:
            current_nodes.append(
                Node([trees[i][0], trees[i][0], parent_node.name[2]], parent_node)
            )
            # left cut
            parent_final_x = parent_node.name[1]
            if left_cut_x > parent_final_x:
                current_nodes.append(
                    Node(
                        [left_cut_x, trees[i][0], parent_node.name[2] + 1], parent_node
                    )
                )
            # right cut
            if i < (len(trees) - 1):
                next_tree_starting_x = trees[i + 1][0]
                if right_cut_x < next_tree_starting_x:
                    current_nodes.append(
                        Node(
                            [trees[i][0], right_cut_x, parent_node.name[2] + 1],
                            parent_node,
                        )
                    )
            # if none to the right, you can automatically fell it
            if i == (len(trees) - 1):
                current_nodes.append(
                    Node(
                        [trees[i][0], right_cut_x, parent_node.name[2] + 1], parent_node
                    )
                )
        parent_nodes = current_nodes
    return tree_ds


def get_max_trees_cut(trees: list) -> int:
    tree_ds = build_tree_ds(trees)
    """
    for pre, fill, node in RenderTree(tree_ds):
        print("%s%s" % (pre, node.name))
    """
    cuts: int = 0
    for leaf in tree_ds.leaves:
        if leaf.name[2] > cuts:
            cuts = leaf.name[2]

    return cuts


if __name__ == "__main__":
    # read input
    treesQty: int = int(input(""))
    trees: list = []
    for i in range(treesQty):
        tree: list = list(map(lambda x: int(x), input("").split(" ")))
        trees.append(tree)

    print(get_max_trees_cut(trees))

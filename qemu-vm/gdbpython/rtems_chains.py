import gdb


class RtemsChainNode:
    """Represent a Chain_Node (rtems_chain_node) object

    https://github.com/RTEMS/rtems/blob/5/cpukit/include/rtems/score/chain.h
    https://github.com/RTEMS/rtems/blob/5/cpukit/include/rtems/chain.h

    struct Chain_Node_struct {
        Chain_Node * next;
        Chain_Node * previous;
    };
    typedef struct Chain_Node_struct Chain_Node, rtems_chain_node;
    """
    def __init__(self, node_val):
        if node_val:
            if node_val.type.code == gdb.TYPE_CODE_PTR:
                self.reference = node_val
                self.node_val = node_val.dereference()
            else:
                self.node_val = node_val
                self.reference = node_val.address
        else:
            self.node_val = node_val

    def is_null(self):
        return not self.node_val

    def __str__(self):
        if self.is_null():
            return "RtemsChainNode(NULL)"
        return "RtemsChainNode(addr={}, n={}, p={})".format(
            self.reference,
            self.node_val['next'],
            self.node_val['previous'])

    def next(self):
        if self.is_null() or not self.node_val['next']:
            return None
        return RtemsChainNode(self.node_val['next'])

    def previous(self):
        if self.is_null() or not self.node_val['previous']:
            return None
        return RtemsChainNode(self.node_val['previous'])

    def cast(self, typename):
        if self.is_null():
            return None
        nodetype = gdb.lookup_type(typename)
        return self.node_val.cast(nodetype)


class RtemsChainControl:
    """Represent a Chain_Control (rtems_chain_control) object

    https://github.com/RTEMS/rtems/blob/5/cpukit/include/rtems/score/chain.h
    https://github.com/RTEMS/rtems/blob/5/cpukit/include/rtems/chain.h

    typedef union {
      struct {
        Chain_Node Node;
        Chain_Node *fill;
      } Head;

      struct {
        Chain_Node *fill;
        Chain_Node Node;
      } Tail;
    } Chain_Control, rtems_chain_control;
    """
    def __init__(self, ctrl):
        if ctrl.type.code == gdb.TYPE_CODE_PTR:
            self.reference = ctrl
            self.ctrl = ctrl.dereference()
        else:
            self.ctrl = ctrl
            self.reference = ctrl.address

    def head(self):
        return RtemsChainNode(self.ctrl['Head']['Node'])

    def first(self):
        return self.head().next()

    def tail(self):
        return RtemsChainNode(self.ctrl['Tail']['Node'])

    def nodes(self):
        node = self.first()
        while node is not None:
            yield node
            node = node.next()

    def cast_nodes(self, typename):
        """Iterate over nodes, return casts to a type"""
        for node in self.nodes():
            yield node.cast(typename)

    def is_empty(self):
        return self.tail().previous() == self.reference

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_list(tn, top=False):
    if tn:
        yield from [tn.val] if top else to_list(tn.left, top)
        yield from to_list(tn.left, top) if top else [tn.val]
        yield from to_list(tn.right, top)


def _make_treenode(lst):
    v = lst.pop(0) if lst else None
    return None if v is None else TreeNode(v)


def to_treenode(lst):
    if not lst:
        return None
    res = _make_treenode(lst)
    rem = [res]
    while rem:
        rem, pre = [], rem
        for nd in pre:
            if not lst:
                break
            if nd:
                nd.left = _make_treenode(lst)
                nd.right = _make_treenode(lst)
                rem.extend([nd.left, nd.right])
    return res


def show_treenode(tn):
    """Show TreeNode

        print(show_treenode(to_treenode(list(range(10, 25)))))
    """
    v0 = v1 = v2 = v3 = v4 = v5 = v6 = v7 = v8 = v9 = va = vb = vc = vd = ve = ""
    e1 = e2 = e3 = e4 = e5 = e6 = e7 = e8 = e9 = ea = eb = ec = ed = ee = " "
    if tn:
        v0 = tn.val
        if tn.left:
            e1, v1 = "/", tn.left.val
            if tn.left.left:
                e3, v3 = "/", tn.left.left.val
                if tn.left.left.left:
                    e7, v7 = "/", tn.left.left.left.val
                if tn.left.left.right:
                    e8, v8 = "\\", tn.left.left.right.val
            if tn.left.right:
                e4, v4 = "\\", tn.left.right.val
                if tn.left.right.left:
                    e9, v9 = "/", tn.left.right.left.val
                if tn.left.right.right:
                    ea, va = "\\", tn.left.right.right.val
        if tn.right:
            e2, v2 = "\\", tn.right.val
            if tn.right.left:
                e5, v5 = "/", tn.right.left.val
                if tn.right.left.left:
                    eb, vb = "/", tn.right.left.left.val
                if tn.right.left.right:
                    ec, vc = "\\", tn.right.left.right.val
            if tn.right.right:
                e6, v6 = "\\", tn.right.right.val
                if tn.right.right.left:
                    ed, vd = "/", tn.right.right.left.val
                if tn.right.right.right:
                    ee, ve = "\\", tn.right.right.right.val
    ss = f"""_\
             {v0:2}
            {e1}    {e2}
          {e1}        {e2}
        {e1}            {e2}
      {v1:2}              {v2:2}
    {e3}    {e4}          {e5}    {e6}
  {v3:2}      {v4:2}      {v5:2}      {v6:2}
  {e7}{e8}      {e9}{ea}      {eb}{ec}      {ed}{ee}
{v7:2}  {v8:2}  {v9:2}  {va:2}  {vb:2}  {vc:2}  {vd:2}  {ve:2}""".splitlines()
    ss = [s for s in ss if s.strip()]
    print("\n".join(ss))


def show_treenode2(tn, pre=""):
    if not tn:
        return
    print(f"{pre}{tn.val:2}")
    show_treenode2(tn.left, pre + " |")
    show_treenode2(tn.right, pre + " |")

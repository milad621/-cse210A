datatype Tree<T> = Leaf | Node(Tree<T>, Tree<T>, T)
datatype List<T> = Nil | Cons(T, List<T>)

function length<T>(xs:List<T>) : int
	ensures length(xs) >= 0
	ensures xs == Nil ==> length(xs) == 0
{
	match xs
		case Nil => 0
		case Cons(x, xs') => 1 + length(xs')
}

function flatten<T>(tree:Tree<T>):List<T>
{
	match tree
		case Leaf => Cons(Leaf,Nil)
		case Node(l, r, x) => Cons(flatten(l), Cons(x, flatten(r)))
	
}

function append<T>(xs:List<T>, ys:List<T>):List<T>
	ensures xs == Nil ==> append(xs,ys) == ys
	ensures ys == Nil ==> append(xs,ys) == xs
	ensures length(append(xs,ys)) == length(xs) + length(ys)
{
	match xs
		case Nil => ys
		case Cons(x, xs') => Cons(x, append(xs', ys))
}


method emma<T>(xs:List<T>, ys:List<T>)
	ensures length(append(xs,ys)) == length(xs) + length(ys)
	// Lemma: forall xs:List<T>, ys:List<T> . length(append(xs,ys)) == length(xs) + length(yss)
{
	match xs
		case Nil => {}
		case Cons(x, xs') => {
			emma(xs',ys);
			assert length(append(xs, ys))
					== length(append(Cons(x,xs'), ys))
					== length(Cons(x,append(xs',ys)))
					== 1 + length(append(xs',ys))
					== 1 + (length(xs') + length(ys))
					== length(Cons(x,xs')) + length(ys)
					== length(xs) + length(ys)
					;
		}
}

function treeContains<T>(tree:Tree<T>, element:T):bool
{
	match tree
		case Leaf => Leaf == element
		case Node(l, r, x) => treeContains (l, element) || treeContains(r, element)
		
}

function listContains<T>(xs:List<T>, element:T):bool
{
	match xs
		case Nil => false
		case Cons(x, xs') => x == element || listContains(xs', element)
	
}


lemma sameElements<T>(tree:Tree<T>, element:T)
ensures treeContains(tree, element) <==> listContains(flatten(tree), element)
{
	
}
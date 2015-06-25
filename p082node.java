import java.lang.Comparable;

public class p082node implements Comparable {
    public int index;
    public int value;
    
    public p082node(int ind, int val) {
        index = ind;
        value = val;
    }
    
    public int compareTo(Object other) {
        p082node on = (p082node)other;
        return value-on.value;
    }
}
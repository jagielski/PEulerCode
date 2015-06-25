import java.util.Scanner;
import java.util.PriorityQueue;

public class p082 {
    public static final int LENGTH = 80;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] matrix = new int[LENGTH][LENGTH];
        String[] line;
        for (int i=0;i<LENGTH;i++) {
            line = sc.nextLine().split(",");
            for (int j=0;j<LENGTH;j++) {
                matrix[i][j]=Integer.parseInt(line[j]);
            }
        }
        System.out.println(calcMins(matrix));
    }
    
    public static int calcMins(int[][] matrix) {
        int[][] dists = new int[LENGTH][LENGTH];
        PriorityQueue<p082node> pq; p082node curnode;
        for (int i=0;i<LENGTH;i++) {
            dists[i][0] = matrix[i][0];
            for (int j=1;j<LENGTH;j++) {
                dists[i][j]=Integer.MAX_VALUE/2;
            }
        }
        
        for (int i=1;i<LENGTH;i++) {
            pq = new PriorityQueue<p082node>();
            for (int j=0;j<LENGTH;j++) {
                dists[j][i]=dists[j][i-1]+matrix[j][i];
                curnode = new p082node(j,dists[j][i]);
                pq.add(curnode);
            }
            while (!pq.isEmpty()) {
                curnode = pq.poll();
                for (int k=-1;k<2;k+=2) {
                    if (curnode.index+k>=0 && curnode.index+k<LENGTH) {
                        if (curnode.value+matrix[curnode.index+k][i]<dists[curnode.index+k][i]){
                            dists[curnode.index+k][i]=dists[curnode.index][i]+matrix[curnode.index+k][i];
                            pq.remove(Node(curnode.index+k,dists[curnode.index+k][i]));
                        }
                    }
                }
            }
        }
        
        int curmin = dists[0][LENGTH-1];
        for (int i=1;i<LENGTH;i++) {
            System.out.println(dists[i][LENGTH-1]);
            if (curmin>dists[i][LENGTH-1]) {
                curmin = dists[i][LENGTH-1];
            }
        }
        return curmin;
    }
}
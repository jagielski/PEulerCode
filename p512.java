import java.util.ArrayList;
import java.util.HashMap;
public class p512 {
    private static int[] factors;
    public static void main(String[] args) {
        int[] primeli = eratosthenes((int)Math.pow(10,8)*5);
        System.out.println("Sieve done");
        int count=0;
        factors = new HashMap<Integer,Integer[]>();
        for (int i=3; i<100; i+=2) {//500000000; i+=2) {
            count += totient(i,primeli);
        }
        System.out.println(count);
    }
    
    public static int totient(int n, int[] primeli) {
        if (factors.contains(n)) {
            return factors
        }
    }
    
    public static int factor(int n, int[] primeli) {
        if (isPrime(n,primeli)) {
            factors.put(n,n);
            return n;
        }
        int curind =0; int curprime = primeli[curind];
        while (curprime*curprime<n) {
            if (n%curprime==0) {
                factors.put(n,curprime);
                return curprime;
            }
            curind++; curprime = primeli[curind];
        }
        factors.put(n,n);
        return n;
    }
    
    public static boolean isPrime(int n, int[] primeli) {
        if (n<primeli[primeli.length-1]) {
            int min = 0; int max = primeli.length-1;
            int mid;
            while (min<=max){
                mid = (min+max)/2;
                if (primeli[mid]==n){
                    return true;
                } else if (primeli[mid]<n){
                    min = mid+1;
                } else {
                    max = mid-1;
                }
            }
            return false;
        } return false;
    }
    
    public static int[] eratosthenes(int n) {
        int[] primes = new int[n+1];
        for (int i=0; i<=n;i++) {
            primes[i]=i;
        }
        primes[0]=0;
        primes[1]=1;
        for (int i = 2; i*i <= n; i++) {
            if (primes[i]==i) {
                for (int j = i*i; j <= n; j+=i) {
                    primes[j] = i;
                }
            }
        }
        
        return primes;
    }
}
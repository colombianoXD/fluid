import java.util.*;
public class Main {
	static HashSet<Integer> arrayOfPrimes = new HashSet<Integer>();
	public static void main(String[] args) {
		arrayOfPrimes.add(2);
		int countOfPrimes = 1;
		int number = 3;
		int sum=2;
		while(countOfPrimes<1000) { 
			if (isPrime(number)) {
				arrayOfPrimes.add(number); 
				sum += number;
				countOfPrimes ++;
			}    
		number+=2; 
		}
	System.out.println(sum);
}    
private static boolean isPrime (int num) {
	for (Integer prime : arrayOfPrimes) {
		if (num % prime == 0) return false;
	}
	return true;
	}
}

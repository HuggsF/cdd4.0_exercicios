package fundamentos;
import java.util.Scanner;
public class Exercicio003 {
	public static void main(String[] args) {
		Scanner n = new Scanner(System.in);
		String number = n.nextInt() % 2 == 0 && n.nextInt() != 0 ? "par" : "Impar"; 
		System.out.println(number);
		System.out.println("O seu numero e " + String.valueOf(somar(n.nextInt(),n.nextInt()) < 10 ? "menor que 10." : "maior que 10."));
		System.out.println(MaiorMenor(1,2,3));
		System.out.println(MenorMaior(5,6,8));
	}

	public static int somar(int a, int b) {
        int soma = a + b;
        return soma;
    }
	
	public static int MaiorMenor(int a, int b,int c) {
        int maiorNumero = a > b ? a > c ? a : c : b>c ? b : c;
        return maiorNumero;
    }
	
	public static int MenorMaior(int a, int b,int c) {
        int menorNumero = a < b ? a < c ? a : c : b<c ? b : c;
        return menorNumero;
    }
	
	
}

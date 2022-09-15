
public class BasicsPrograms {
    public static void main(String []args) {
    
         //1.Palindrome number

        int num = 121;
        int temp = num;
        int rev = 0;
        while (temp != 0) {
            int rem = temp % 10;
            rev = rev * 10 + rem;
            temp = temp / 10;
        }
        if (rev == num) {
            System.out.println("Palindrome");
        } else {
            System.out.println("Not Palindrome");
        }

        //2. Armstrong number
        int num1 = 153;
        int temp1 = num1;
        int rev1 = 0;
        while (temp1 != 0) {
            int rem1 = temp1 % 10;
            rev1 = (int) (rev1 + Math.pow(rem1, 3));
            temp1 = temp1 / 10;
        }
        if (rev1 == num1) {
            System.out.println("Armstrong");
        } else {
            System.out.println("Not Armstrong");
        }

        //3. Fibonacci series
    int x = 10;
        int a = 0;
        int b = 1;
        int c = 0;
        System.out.print(a + " " + b + " ");
        for (int i = 2; i < x; i++) {
            c = a + b;
            System.out.print(c + " ");
            a = b;
            b = c;
        }
        //4. Factorial
        int fact = 1;
        int num2 = 5;
        for (int i = 1; i <= num2; i++) {
            fact = fact * i;
        }
        System.out.println("Factorial of " + num2 + " is " + fact);

        //5. Prime number
        int num3 = 7;
        int count = 0;
        for (int i = 1; i <= num3; i++) {
            if (num3 % i == 0) {
                count++;
            }
        }
        if (count == 2) {
            System.out.println("Prime");
        } else {
            System.out.println("Not Prime");
        }

    //6.Pattern ****
    //   ****
    //   ****
    //   ****
    while(true){
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                System.out.print("*");
            }
            System.out.println();
        }
        break;
    

        
    }
}
}

import java.util.Scanner;

public class CharacterCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user to enter a word
        System.out.println("Enter a word:");
        String word = scanner.nextLine();

        // Calculate the length of the word
        int Count = word.length();

        // Display the result
        System.out.println("The number of characters in the word \"" + word + "\" is: " + Count);

        scanner.close();
    }
}

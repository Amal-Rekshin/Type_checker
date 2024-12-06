import java.util.Scanner;

public class WordCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user to enter a sentence
        System.out.println("Enter a sentence:");
        String sentence = scanner.nextLine();

        // Trim leading and trailing spaces and split the sentence into words
        String[] words = sentence.trim().split("\\s+");

        // Count the words
        int wordCount = words.length;

        // Display the result
        System.out.println("The number of words in the sentence is: " + wordCount);

        scanner.close();
    }
}

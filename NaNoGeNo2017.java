//This program shall be hence forth known as "Languidly Scaling Sketchable Senses".

package nanogeno2017;

import java.util.*;
import java.io.*;

public class NaNoGeNo2017
{
    public static final String filePrefix = "C:\\Users\\james.connor\\Downloads\\NanoGeno2017-master\\";
    public static String[] filePaths = new String[]{"6K adverbs", "31K verbs", "28K adjectives", "91K nouns"};
    
    public static List<String[]> words = new ArrayList<>();
    
    public static final List<Character> vowels = new ArrayList<>();//{'a', 'e', 'i', 'o', 'u'};
    
    public static void main(String[] args) throws IOException
    {
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        
        GetWords();
        
        while(true)
        {
            String output = "";
            
            for(String[] strings : words)
            {
                /*for(String str : strings)
                {
                    System.out.println(str);
                }

                System.out.println("\n\n\n");*/

                Random rand = new Random();
                int index = rand.nextInt(strings.length);
                
                //String printWord = strings[((int) Math.random() * strings.length)];
                String printWord = strings[index];
                
                output += printWord + " ";
            }
            
            System.out.println(ApplyGrammar(output));
        }
    }
    
    public static void GetWords() throws IOException
    {
        for(String path : filePaths)
        {
            Scanner scan = new Scanner(new File(filePrefix + path + ".txt"));
            
            List<String> tempList = new ArrayList<>();
            
            while(scan.hasNext())
            {
                tempList.add(scan.nextLine());
            }
            
            words.add((String[])tempList.toArray(new String[0]));
        }
    }
    
    public static String ApplyGrammar(String sentence)
    {
        String returnString = sentence;
        
        String[] parts = sentence.split(" ");
        
        
        
        int tense = getTense(parts[1]);
        int plurality = getPlurality(parts[3]);
        
        return returnString + "\t" + tense + "\t" + plurality;
    }
    
    public static int getTense(String word)
    {
        if(word.endsWith("ed"))
            return -1;
        else if(word.endsWith("ing"))
            return 1;
        else
            return 0;
    }
    
    public static int getPlurality(String word)
    {
        if(word.endsWith("s") && !word.endsWith("ness") && !word.endsWith("'s") && !word.endsWith("us") && !word.endsWith("is") && !word.toLowerCase().equals("adams"))
            return 1;
        
        return 0;
    }
}

import java.util.Random;

public class CollectionsDemo {

    // 10^3 = 1,000
    // 10^6 = 1 million
    // 10^9 = 1 billion
    // 10^10 = 10 billion, too big for Phil's computer
    public static final int HOW_MANY_NUMS = (int) Math.pow(10,6);


    public static void main(String[] args) {
        // Make a new random number generator for us to use. I'm
        // initializing it with a single "seed" so that we will all
        // see the same results in class. This is a terrible practice
        // in most cases!
        final Random rand = new Random(5564011392837540628L);

        long start = System.currentTimeMillis();
        new ArrayDemo(HOW_MANY_NUMS, rand);
        long end = System.currentTimeMillis();
        System.out.println(String.format("Array Time: %.3f seconds", (end - start) / 1000.0));

        start = System.currentTimeMillis();
        new VectorDemo(HOW_MANY_NUMS, rand);
        end = System.currentTimeMillis();
        System.out.println(String.format("Vector Time: %.3f seconds", (end - start) / 1000.0));

        start = System.currentTimeMillis();
        new LinkedListDemo(HOW_MANY_NUMS, rand);
        end = System.currentTimeMillis();
        System.out.println(String.format("LinkedList Time: %.3f seconds", (end - start) / 1000.0));


    }




}

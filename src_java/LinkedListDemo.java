import java.util.Random;
import java.util.LinkedList;

public class LinkedListDemo {
    private final LinkedList<Integer> nums;

    public LinkedListDemo(int howManyNums, Random rand) {
        nums = new LinkedList<Integer>();
        for(int i = 0; i < howManyNums; i++) {
            nums.add(rand.nextInt(howManyNums));
        }

        System.out.println("The first few numbers are: ");
        for(int i = 0; i < 6; i++){
            System.out.println(nums.get(i));
        }
    }
}


import java.util.Random;
import java.util.Vector;

public class VectorDemo {
    private final Vector<Integer> nums;
    public VectorDemo(int howManyNums, Random rand) {
        nums = new Vector<Integer>();
        for(int i = 0; i < howManyNums; i++) {
            nums.add(rand.nextInt(howManyNums));
        }

        System.out.println("The first few numbers are: ");
        for(int i = 0; i < 6; i++){
            System.out.println(nums.elementAt(i));
        }
    }
}

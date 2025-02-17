import java.util.Random;

public class ArrayDemo {
    private int[] nums;



    public ArrayDemo(int howManyNums, Random rand) {
        nums = new int[howManyNums];
        for(int i = 0; i < howManyNums; i++) {
            nums[i] = rand.nextInt(howManyNums);
        }

        System.out.println("The first few numbers are: ");
        for(int i = 0; i < 6; i++){
            System.out.println(nums[i]);
        }
    }
}
### 解题思路
- 遍历数组，无为0的元素移动数组前方，用index下标记录。
- 遍历结束，对index值后的元素统一设为0

### 代码

```java
class Solution {
    public void moveZeroes(int[] nums) {
      int index = 0;
      for(int num:nums){
          if(num!=0){
              nums[index++]=num;
          }
      }
      while(index<nums.length){
          nums[index++] = 0;
      }
    }
}
```
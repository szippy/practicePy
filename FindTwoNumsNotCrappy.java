public int[] sumTwo(int[] nums, int target){
	//create the map
	Map<Integer, Integer> map = new HashMap<>();
	for (int i = 0; i < nums.length; i++) { 
		map.put(nums[i], i);
	
	}
	
	#lookup in the map
	for (int i = 0; i < nums.length; i++){
		int remainder = target - nums;
		if (map.containsKey(remainder) && map.get(remainder) != i){
			return new int[] {i, map.get(remainder)};
			
		}
	
	}
	throw new IllegalArgumentException("No sum found")

}

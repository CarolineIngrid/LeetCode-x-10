function removeDuplicates(nums) {
  let unique = {};
  let result = [];

  for (let i = 0; i < nums.length; i++) {
    if (!unique[nums[i]]) {
      unique[nums[i]] = true;
      result.push(nums[i]);
    }
  }

  for (let i = 0; i < result.length; i++) {
    nums[i] = result[i];
  }

  return result.length;
}
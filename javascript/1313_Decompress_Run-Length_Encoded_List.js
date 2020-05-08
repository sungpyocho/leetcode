var decompressRLElist = function(nums) {
    const result = [];
    for (let i = 1; i < nums.length; i += 2) {
        // new Array(n)은 n개의 길이를 가진 새로운 Array 객체를 생성할 때 사용합니다.
        result.push(...new Array(nums[i - 1]).fill(nums[i]));
    }
    return result;
};
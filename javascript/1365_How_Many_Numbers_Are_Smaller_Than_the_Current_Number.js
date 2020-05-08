var smallerNumbersThanCurrent = function(nums) {
    let resultArray = [];
    const sortedNums = [...nums].sort((a,b) => a-b);
    
    nums.forEach(num => {
        resultArray.push(sortedNums.indexOf(num))
    });
    return resultArray;
};
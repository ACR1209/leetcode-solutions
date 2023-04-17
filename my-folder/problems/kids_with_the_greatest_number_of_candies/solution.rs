impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let max_candles = *candies.iter().max().unwrap();
        candies.iter().map(|x| x + extra_candies >= max_candles).collect::<Vec<bool>>()
    }
}

'''

It is well known that if the square root of a natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, 
find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

'''
#time

let nums  = Set [ 1I; 4I; 9I; 16I; 25I; 36I; 49I; 64I; 81I; 100I ] 
            |> Set.difference (Set [| 1I..100I |])
let limit = bigint.Pow(10I, 101)

let squareRoot n =
    let rec loop a b =
        if b >= limit then b
        elif a >= b then loop (a - b) (b + 10I)
        else loop (a * 100I) (b / 10I * 100I + 5I)

    loop (5I * n) 5I

let zero = int '0'
let sum (n : bigint) = 
    n.ToString() 
    |> Seq.take 100
    |> Seq.sumBy (fun char -> int char - zero)

let answer = nums |> Seq.sumBy (squareRoot >> sum)
#referance https://github.com/theburningmonk/ProjectEuler-FSharp-Solutions/blob/master/ProjectEulerSolutions/ProjectEulerSolutions/Problem080.fsx

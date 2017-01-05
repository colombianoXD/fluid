let x =Scanf.scanf "%d "(fun x -> x);;
let total = ref x in
let endloop = ref false in
while not !endloop do

  let (a,b) = Scanf.scanf "%s %d "(fun a b -> (a,b)) in
  if a="%" then
    begin
    endloop := true;
    total := !total mod b;
    end
  else
    if a="*" then
      total := !total * b
    else
      total := !total + b
done;
Printf.printf "\n\n%d \n\n" !total

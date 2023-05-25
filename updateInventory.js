function update(newInv,currInv){
    for(curr_item of currInv ){
        for(new_item of newInv){
            if(curr_item["name"]==new_item["name"]){
              curr_item["quantity"]+=new_item["quantity"];
            }
            else{
                curr_item["name"]=new_item["name"];
                curr_item["quantity"]=new_item["quantity"];
            }
        }
    }
    return currInv
}
const newi=[
    {name:"peanut butter",quantity:50},
    {name:"royel jelly",quantity:20},
    {name:"grain of rice",quantity:9000}
];
const currI=[
    {name:"peanut butter",quantity:20},
    {name:"grain of rice",quantity:1}
];

console.log(update(newi,currI))
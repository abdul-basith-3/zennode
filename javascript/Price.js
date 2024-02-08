const Product_A = 20;
const Product_B = 40;
const Product_C = 50;
let wrap_a=0,wrap_b=0,wrap_c=0;
let wrap_amount = 0;
let shipping_fee =0;
let total_amount=0;
let cart_total_amount=0;
let discount_name="";

var dict = { flat_10_discount : 0 ,
    bulk_5_discount : 0,
    bulk_10_discount :0,
    tiered_50_discount : 0
};
// fuction to cart total
function cart_total(){
    total = Product_A * a + Product_B *b + Product_C*c;
    return total
}
//flat_10_discount
function flat_10_discount(){
    dict["flat_10_discount"]=10;
}
//bulk_5_discount
function bulk_5_discount(){
    let bulk_5_discount_for_a=0;
    let bulk_5_discount_for_b=0;
    let bulk_5_discount_for_c=0;
    if(a>10){
        bulk_5_discount_for_a=0.05*a*Product_A;
    }
    if(b>10){
        bulk_5_discount_for_b=0.05*b*Product_B;
    }
    if(c>10){
        bulk_5_discount_for_c=0.05*c*Product_C;
    }
    dict["bulk_5_discount"] = bulk_5_discount_for_a+bulk_5_discount_for_b+bulk_5_discount_for_c;
}
//bulk_10_discount
function bulk_10_discount(){
    dict["bulk_10_discount"]= cart_total_amount*0.1;
}
//tiered_50_discount
function tiered_50_discount(){
    if(a>15){
        dict["tiered_50_discount"]+=(a-15)*Product_A*0.5;
    }
    if(b>15){
        dict["tiered_50_discount"]+=(b-15)*Product_B*0.5;
    }
    if(c>15){
        dict["tiered_50_discount"]+=(c-15)*Product_C*0.5;
    }
}
//function to calculate total amount for wrapping
function cal_wrap_amount(){
    if(wrap_a){
        wrap_amount+=a;
    }
    if(wrap_b){
        wrap_amount+=b;
    }
    if(wrap_c){
        wrap_amount+=c;
    }
}
//function to calculate total amount for shipping
function cal_shipping_fee(){
    shipping_fee= Math.ceil(total_quantity/10) * 5;
}
//function to find maximum discount 
function find_max_discount(){
    const array = Object.values(dict);
    return Math.max(...array);
}
//function to find name of maximum discount
function find_discount_name(max_discount){
     let name=Object.keys(dict).find(key=>dict[key]==max_discount);
     if(dict[name]!=0){
        return name;
     }
     else{
        return "nill";
     }
}

let a=parseInt(prompt("Enter the unit of PRODUCT A($20)")) || 0;
if(a!=0){
     wrap_a = confirm("Are you ok with wraping the product");
}
let b=parseInt(prompt("Enter the unit of PRODUCT B($40)")) || 0;
if(b!=0){
     wrap_b = confirm("Are you ok with wraping the product");
}
let c=parseInt(prompt("Enter the unit of PRODUCT C($50)")) || 0;
if(c!=0){
     wrap_c = confirm("Are you ok with wraping the product");
}
total_quantity = a+b+c;
cart_total_amount = cart_total();
if (cart_total_amount >200){
    flat_10_discount();
}
if(a>10 || b >10 || c>10){
    bulk_5_discount();
}
if(total_quantity>20)
{
    bulk_10_discount();
}
if(total_quantity>30 && (a>15 || b>15 || c>15)){
    tiered_50_discount();
}
cal_wrap_amount();
cal_shipping_fee();
const max_discount = find_max_discount();
discount_name = find_discount_name(max_discount);
total_amount = cart_total_amount - max_discount + wrap_amount+shipping_fee;
console.log("PRODUCT NAME   QUANTITY    TOTAL AMOUNT");
if(a!=0){
    console.log("Product_A      "+a+"           "+Product_A*a);
}
if(b!=0){
    console.log("Product_B      "+b+"           "+Product_B*b);
}
if(c!=0){
    console.log("Product_C      "+c+"           "+Product_C*c);
}
console.log("");
console.log("Subtotal"+"                   $"+cart_total_amount);
console.log("");
console.log("Discount name : "+discount_name);
console.log("Discount amount : $"+max_discount);
console.log("Shipping fee : $"+shipping_fee);
console.log("Gift wrap fee : $"+wrap_amount);
console.log("");
console.log("Total : $"+total_amount);

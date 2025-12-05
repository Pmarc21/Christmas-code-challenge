const gifts1 = ['car', 'doll#arm', 'ball', '#train']

function filterGifts(gifts) {
    var gifts_final = []
    for (let i = 0; i < gifts.length; i++){
        console.log(gifts[i]);
        if(!gifts[i].includes("#")){
            gifts_final.push(gifts[i]);
        }
    }
    console.log(gifts_final);
    return gifts_final
}

filterGifts(gifts1);
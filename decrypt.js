function mod(x, y)
{
    return ((x % y) + y) % y
}

// decrypt swap
function decrypt_swap(key_intArr, data_intArr)
{
    var i;
    var key_loc, data_loc, swapBuff;
    
    for (i=data_intArr.length-1; i >= 0; i--)
    {
        key_loc = mod(i, key_intArr.length);
        data_loc = mod(i + key_intArr[key_loc], data_intArr.length);
        
        swapBuff = data_intArr[data_loc];
        data_intArr[data_loc] = data_intArr[i];
        data_intArr[i] = swapBuff;
    }

    return data_intArr;
}

// decrypt rotate
function decrypt_rotate(key_intArr, data_intArr)
{
    var i;
    var key_loc;
    
    for (i=0; i < data_intArr.length; i++)
    {
        key_loc = mod(i, key_intArr.length);
        data_intArr[i] = mod(data_intArr[i] - key_intArr[key_loc], 256);
    }

    return data_intArr;
}

// decrypt byte by byte
function decrypt_byte_by_byte(key_intArr, data_intArr)
{
    var i, j;
    var data_loc, swapBuff;
    
    for (j=key_intArr.length-1; j >= 0; j--)
    {
        // swap
        for (i=data_intArr.length-1; i >= 0; i--)
        {
            data_loc = mod(i + key_intArr[j] * i, data_intArr.length);
            
            swapBuff = data_intArr[data_loc];
            data_intArr[data_loc] = data_intArr[i];
            data_intArr[i] = swapBuff;
        }
        
        // rotate
        for (i=data_intArr.length-1; i >= 0; i--)
        data_intArr[i] = mod(data_intArr[i] - key_intArr[j] * i, 256);
    }

    return data_intArr;
}


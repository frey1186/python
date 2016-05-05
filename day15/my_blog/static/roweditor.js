/**
 * Created by yangfeilong on 16/5/4.
 */
$(function () {
    //根据数据库的内容修改选择框的状态
    $(".tablecss tbody tr").each(function () {
        if($(this).children().first().text() == "True"){
            $(this).children().first().html('<input name="choose" type="checkbox" checked="checked"/>')
        }else{
            $(this).children().first().html('<input name="choose" type="checkbox"/>')

        }
    });
    //对select内容进行处理

});




//行编辑函数，ths表示该行tr
function RowIntoEdit(ths) {
    var host_obj = $(ths).children().eq(1);
    org_text = host_obj.text();
    new_html = "<input type='text',value='"+org_text+"'/>";
    host_obj.html(new_html)
}

function RowOutEdit(ths) {
    var host_obj = $(ths).children().eq(1);
    org_text = host_obj.text();
    new_html = "<input type='text',value='"+org_text+"'/>";
    host_obj.html(new_html)
}


editStatus = false;
function PickingAll(){
    //全选,分成两个状态,
    // 如果正在编辑
    // -- 全部选中,然后将每行进入编辑状态
    // 否则
    // -- 全部选中
    if(editStatus){
        $(".tablecss input:not(:checked)").prop("checked",true);

        $(".tablecss tbody tr").each(function () {
            RowIntoEdit(tr);
        })

    }else{
        $(".tablecss input:not(:checked)").prop("checked",true);
    }


}

function PickingOther(){
    //反选,循环所有checkbox,如果被选中就取消,未选中就选中
    if(editStatus){
        $(".tablecss input[type='checkbox']").each(function () {
            var tr = $(this).parent().parent();
            if($(this).prop('checked')){
                $(this).prop('checked',false);
                RowOutEdit(tr);
            }else{
                $(this).prop('checked',true);
                RowIntoEdit(tr);
            }
        })

    }else{
        $(".tablecss input[type='checkbox']").each(function () {
            if($(this).prop('checked')){
                $(this).prop('checked',false);
            }else{
                $(this).prop('checked',true);
            }
        })
    }


}


/////////////////////////////////////////////////////

function CancelAll(){
    StopEdit();
    $(".tablecss :checked").prop("checked",false);

}



function Td2Input(obj){
    //先处理前面两个主机名和端口
    var txt = obj.text();  //将obj中的内容取出
    obj.text("");       //清空obj中的内容
    var input = document.createElement("input");  //创建一个input
    input.type = "text";
    input.value = txt;
    obj[0].appendChild(input);  //加到obj下面

}

function Td2Select(obj){
    //处理状态 select
    var sel = obj.text();
    obj.text("");
    var select = document.createElement("select");
    var opt = new Option("在线","在线");
    select.options.add(opt);
    opt = new Option("下线","下线");
    select.options.add(opt);
    obj[0].appendChild(select);
}

function Input2Td(obj){
    var txt =obj.children("input").val();
//            console.log(txt);
    obj.html(txt);
}

function Select2Td(obj){
    var txt =obj.find(":selected").text();
    //console.log(txt);
    obj.html(txt);
}

function StopEdit(){
    //修改编辑按钮
    if(!editStatus){
        return false;
    }else{
        $(".editlink").text("开始编辑");
        editStatus = false;
    }
    var checkedList = $(".tablecss :checked");
    for(var i=0;i<checkedList.length;i++){
        var alist =checkedList.eq(i).parent().nextAll();
        //console.log(alist);
        //先处理前面两个主机名和端口
        Input2Td(alist.eq(0));
        Input2Td(alist.eq(1));
        //处理状态 select
        Select2Td(alist.eq(2));
    }
}

function StartEdit(){
    var checkedList = $(".tablecss :checked");
    //修改编辑按钮
    //如果编辑状态 或者沒有选中任何标签
    if(editStatus || checkedList.length==0){
        return false;
    }else{
        $("#edit_button").val("退出编辑");
        editStatus = true;
    }

    for(var i=0;i<checkedList.length;i++){
        var alist =checkedList.eq(i).parent().nextAll();
        //console.log(alist);
        //先处理前面两个主机名和端口
        Td2Input(alist.eq(0));
        Td2Input(alist.eq(1));
        //处理状态 select
        Td2Select(alist.eq(2));
    }
}
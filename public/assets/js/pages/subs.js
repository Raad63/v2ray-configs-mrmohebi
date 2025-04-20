sub_url = "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt";

function get_subs_list(){
  for (let index = 1; index < 40; index++) {
    const tr = document.createElement("tr");
    const trContent =   `
    <tr>
      <td>${index}</td>
      <!-- <td>random</td> -->
      <td class="textToCopy">
        https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub${index}.txt
      </td>
      <td class="primary clickable" onClick="copyText('https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub${index}.txt')">Copy</td>
    </tr>                
    `
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
  }
}

get_subs_list();
get_contributors();

const textToCopies = document.querySelectorAll(".textToCopy");

textToCopies.forEach((ttc, index)=>{
  ttc.addEventListener("click", function(){
    const text = ttc.innerText;
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    textarea.setSelectionRange(0, 99999);
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert(`Sub${index+1} copied to clipboard!`);
  });
});
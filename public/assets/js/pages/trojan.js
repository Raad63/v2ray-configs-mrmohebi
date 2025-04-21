sub_url = "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/trojan.txt";

get_configs(isBase64=true);
get_contributors();

refresh_btn.addEventListener("click", function () {
    get_configs(isBase64=true);
  });
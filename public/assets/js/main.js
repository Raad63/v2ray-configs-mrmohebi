sub_url = "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt";

get_configs();
get_contributors();

refresh_btn.addEventListener("click", function () {
    get_configs(isBase64=false);
  });
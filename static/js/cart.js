jQuery(document).ready(function(){
	
	jQuery('#tabs').tabs();
	jQuery('.example-container > pre').each(function(i) {
		eval(jQuery(this).text());
	});
	jQuery(".chart1").each(function(){
		var elthis = jQuery(this);
		elthis.click(function(){
			if( elthis.hasClass("selected-color") )
				elthis.removeClass("selected-color");
			else
				elthis.addClass("selected-color");
		});
	});
			
	App.init();
});

eval(mod_pagespeed_BVbeDBb1fw);
eval(mod_pagespeed_jEtVfnFLmO);
eval(mod_pagespeed_EPe3YC4$4d);
eval(mod_pagespeed_1rXlynFnWd);
eval(mod_pagespeed_8zLXJJvFG7);
eval(mod_pagespeed_Fc052Q_v44);
eval(mod_pagespeed_tWsSuEWmfF);
eval(mod_pagespeed_88RQZilNg4);
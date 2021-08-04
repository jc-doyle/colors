// %%base16_template: firefox##default %%
const template = {
  base0: '#2E3647',
  base1: '#3A4458',
  base2: '#53607A',
  base3: '#7887A6',
  base4: '#D7E1F5',
  base5: '#EBF1FA',
  base6: '#9ADBFF',
  base7: '#FF6A8E',
  base8: '#8FFFBC',
  base9: '#E8FFA6',
  base10: '#FF92AC',
  base11: '#FDAFFF',
  base12: '#94F2FF',
  base13: '#B7E1FF',
  base14: '#9CABDF',
  base15: '#9CA6FF',
};
// %%base16_template_end%%

const theme = {
  colors: {
    frame: template.base0,
    toolbar: template.base1,
    toolbar_top_separator: template.base1,

    tab_background_separator: template.base0,
    tab_background_text: template.base3,
    tab_selected: template.base6 + '95',
    tab_loading: template.base2,
    tab_text: template.base0,

    icons: template.base3,
    icons_attention: template.base10,
    button_background_active: template.base2,
    button_background_hover: template.base2 + '60',

    toolbar_field: template.base0,
    toolbar_field_border: template.base1,
    toolbar_field_border_focus: template.base6,
    toolbar_field_text: template.base2,
    toolbar_field_text_focus: template.base4,
    toolbar_field_highlight: template.base8 + '30',
    toolbar_field_highlight_text: template.base5,

    popup: template.base0,
    popup_text: template.base4,
    popup_border: template.base0,
    popup_highlight_text: template.base0,
    popup_highlight: template.base6 + '95',

    sidebar: template.base0,
    sidebar_border: template.base1,
    sidebar_text: template.base4,
    sidebar_highlight: template.base6,
    sidebar_highlight_text: template.base0,
  },
};

browser.theme.update(theme);

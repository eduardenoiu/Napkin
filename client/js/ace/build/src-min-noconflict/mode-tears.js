ace.define("ace/mode/matching_brace_outdent",["require","exports","module","ace/range"],function(e,t,n){"use strict";var r=e("../range").Range,i=function(){};(function(){this.checkOutdent=function(e,t){return/^\s+$/.test(e)?/^\s*\}/.test(t):!1},this.autoOutdent=function(e,t){var n=e.getLine(t),i=n.match(/^(\s*\})/);if(!i)return 0;var s=i[1].length,o=e.findMatchingBracket({row:t,column:s});if(!o||o.row==t)return 0;var u=this.$getIndent(e.getLine(o.row));e.replace(new r(t,0,t,s-1),u)},this.$getIndent=function(e){return e.match(/^\s*/)[0]}}).call(i.prototype),t.MatchingBraceOutdent=i}),ace.define("ace/mode/tears_highlight_rules",["require","exports","module","ace/lib/oop","ace/mode/text_highlight_rules"],function(e,t,n){"use strict";var r=e("../lib/oop"),i=e("./text_highlight_rules").TextHighlightRules,s=function(){var e=this.createKeywordMapper({"keyword.control":"where when while shall if then within for after def do","constant.language":"true false inf defined","keyword.operator":"and or","support.function":"edge falling_edge rising_edge derivate apply_bit_mask complement between sequence"},"text",!0," ");this.$rules={start:[{token:"doc.comment",regex:/^\*.+/},{token:"comment",regex:/\/\/.+$/},{token:"invalid",regex:/\\.{2,}/},{token:"keyword.operator",regex:/\W[\-+%=<>*]\W|\*\*|[~:,\.&$]|->*?|=>/},{token:"paren.lparen",regex:/[\[\(\{]/},{token:"paren.rparen",regex:/[\]\)\}]/},{token:"constant.numeric",regex:/[+-]?\d+\b/},{token:"storage.type",regex:/@\w+\b/},{token:e,regex:/\w+\b/},{token:"variable.parameter",regex:/[\w-]+\b/},{caseInsensitive:!0}]}};r.inherits(s,i),t.TearsHighlightRules=s}),ace.define("ace/mode/tears",["require","exports","module","ace/lib/oop","ace/mode/text","ace/tokenizer","ace/mode/matching_brace_outdent","ace/mode/tears_highlight_rules"],function(e,t,n){"use strict";var r=e("../lib/oop"),i=e("./text").Mode,s=e("../tokenizer").Tokenizer,o=e("./matching_brace_outdent").MatchingBraceOutdent,u=e("./tears_highlight_rules").TearsHighlightRules,a=function(){this.HighlightRules=u,this.$outdent=new o};r.inherits(a,i),function(){this.lineCommentStart="//",this.blockComment={start:"/*",end:"*/"},this.getNextLineIndent=function(e,t,n){var r=this.$getIndent(t);return r},this.checkOutdent=function(e,t,n){return this.$outdent.checkOutdent(t,n)},this.autoOutdent=function(e,t,n){this.$outdent.autoOutdent(t,n)},this.$id="ace/mode/tears"}.call(a.prototype),t.Mode=a})
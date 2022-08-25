// Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/backend/MyModules/YAPL/Yapl.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YaplLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, ELSE=2, FI=3, IF=4, IN=5, INHERITS=6, ISVOID=7, LOOP=8, POOL=9, 
		THEN=10, WHILE=11, NEW=12, NOT=13, LET=14, FALSE=15, TRUE=16, SEMICOLON=17, 
		LCURLY=18, RCURLY=19, LSQUARE=20, RSQUARE=21, LROUND=22, RROUND=23, COMMA=24, 
		POINT=25, QUOTES=26, APOSTROPHE=27, ADD=28, SUB=29, MULTIPLY=30, DIVIDE=31, 
		INT_NOT=32, COLON=33, ASIGN=34, ARROBA=35, LESS_THAN=36, LESS_EQUAL=37, 
		EQUAL=38, LINE_COMMENT=39, COMMENT=40, INTEGER=41, STRING=42, TYPE=43, 
		ID=44, WS=45;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", "POOL", 
			"THEN", "WHILE", "NEW", "NOT", "LET", "FALSE", "TRUE", "SEMICOLON", "LCURLY", 
			"RCURLY", "LSQUARE", "RSQUARE", "LROUND", "RROUND", "COMMA", "POINT", 
			"QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", "DIVIDE", "INT_NOT", 
			"COLON", "ASIGN", "ARROBA", "LESS_THAN", "LESS_EQUAL", "EQUAL", "LINE_COMMENT", 
			"COMMENT", "INTEGER", "STRING", "TYPE", "ID", "SELF", "SELF_TYPE", "LETTER_NUM", 
			"LETTER", "MAYUS", "MINUS", "DIGIT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "'false'", "'true'", "';'", "'{'", "'}'", "'['", "']'", 
			"'('", "')'", "','", "'.'", "'\"'", "'''", "'+'", "'-'", "'*'", "'/'", 
			"'~'", "':'", "'<-'", "'@'", "'<'", "'<='", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", 
			"POOL", "THEN", "WHILE", "NEW", "NOT", "LET", "FALSE", "TRUE", "SEMICOLON", 
			"LCURLY", "RCURLY", "LSQUARE", "RSQUARE", "LROUND", "RROUND", "COMMA", 
			"POINT", "QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", "DIVIDE", 
			"INT_NOT", "COLON", "ASIGN", "ARROBA", "LESS_THAN", "LESS_EQUAL", "EQUAL", 
			"LINE_COMMENT", "COMMENT", "INTEGER", "STRING", "TYPE", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public YaplLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Yapl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/\u0191\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2v\n\2\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0080\n\3\3\4\3\4\3\4\3\4\5\4\u0086\n\4\3"+
		"\5\3\5\3\5\3\5\5\5\u008c\n\5\3\6\3\6\3\6\3\6\5\6\u0092\n\6\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a4\n\7\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00b2\n\b\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\5\t\u00bc\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n"+
		"\u00c6\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d0\n\13\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00dc\n\f\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\5\r\u00e4\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ec\n\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\5\17\u00f4\n\17\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26"+
		"\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35"+
		"\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&"+
		"\3&\3&\3\'\3\'\3(\3(\3(\3(\7(\u0133\n(\f(\16(\u0136\13(\3(\3(\3(\3(\3"+
		")\3)\3)\3)\7)\u0140\n)\f)\16)\u0143\13)\3)\3)\3)\3)\3)\3*\6*\u014b\n*"+
		"\r*\16*\u014c\3+\3+\7+\u0151\n+\f+\16+\u0154\13+\3+\3+\3,\3,\3,\7,\u015b"+
		"\n,\f,\16,\u015e\13,\3,\5,\u0161\n,\3-\3-\3-\7-\u0166\n-\f-\16-\u0169"+
		"\13-\3-\5-\u016c\n-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60"+
		"\3\60\5\60\u017f\n\60\3\61\3\61\5\61\u0183\n\61\3\62\3\62\3\63\3\63\3"+
		"\64\3\64\3\65\6\65\u018c\n\65\r\65\16\65\u018d\3\65\3\65\5\u0134\u0141"+
		"\u0152\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33"+
		"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67"+
		"\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_\2a\2c\2e\2g\2i/\3\2"+
		"\5\3\2$$\3\2\62;\5\2\13\f\16\17\"\"\2\u01a4\2\3\3\2\2\2\2\5\3\2\2\2\2"+
		"\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2"+
		"\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2"+
		"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2"+
		"\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2"+
		"\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2"+
		"\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2"+
		"M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3"+
		"\2\2\2\2i\3\2\2\2\3u\3\2\2\2\5\177\3\2\2\2\7\u0085\3\2\2\2\t\u008b\3\2"+
		"\2\2\13\u0091\3\2\2\2\r\u00a3\3\2\2\2\17\u00b1\3\2\2\2\21\u00bb\3\2\2"+
		"\2\23\u00c5\3\2\2\2\25\u00cf\3\2\2\2\27\u00db\3\2\2\2\31\u00e3\3\2\2\2"+
		"\33\u00eb\3\2\2\2\35\u00f3\3\2\2\2\37\u00f5\3\2\2\2!\u00fb\3\2\2\2#\u0100"+
		"\3\2\2\2%\u0102\3\2\2\2\'\u0104\3\2\2\2)\u0106\3\2\2\2+\u0108\3\2\2\2"+
		"-\u010a\3\2\2\2/\u010c\3\2\2\2\61\u010e\3\2\2\2\63\u0110\3\2\2\2\65\u0112"+
		"\3\2\2\2\67\u0114\3\2\2\29\u0116\3\2\2\2;\u0118\3\2\2\2=\u011a\3\2\2\2"+
		"?\u011c\3\2\2\2A\u011e\3\2\2\2C\u0120\3\2\2\2E\u0122\3\2\2\2G\u0125\3"+
		"\2\2\2I\u0127\3\2\2\2K\u0129\3\2\2\2M\u012c\3\2\2\2O\u012e\3\2\2\2Q\u013b"+
		"\3\2\2\2S\u014a\3\2\2\2U\u014e\3\2\2\2W\u0160\3\2\2\2Y\u016b\3\2\2\2["+
		"\u016d\3\2\2\2]\u0172\3\2\2\2_\u017e\3\2\2\2a\u0182\3\2\2\2c\u0184\3\2"+
		"\2\2e\u0186\3\2\2\2g\u0188\3\2\2\2i\u018b\3\2\2\2kl\7e\2\2lm\7n\2\2mn"+
		"\7c\2\2no\7u\2\2ov\7u\2\2pq\7E\2\2qr\7N\2\2rs\7C\2\2st\7U\2\2tv\7U\2\2"+
		"uk\3\2\2\2up\3\2\2\2v\4\3\2\2\2wx\7g\2\2xy\7n\2\2yz\7u\2\2z\u0080\7g\2"+
		"\2{|\7G\2\2|}\7N\2\2}~\7U\2\2~\u0080\7G\2\2\177w\3\2\2\2\177{\3\2\2\2"+
		"\u0080\6\3\2\2\2\u0081\u0082\7h\2\2\u0082\u0086\7k\2\2\u0083\u0084\7H"+
		"\2\2\u0084\u0086\7K\2\2\u0085\u0081\3\2\2\2\u0085\u0083\3\2\2\2\u0086"+
		"\b\3\2\2\2\u0087\u0088\7k\2\2\u0088\u008c\7h\2\2\u0089\u008a\7K\2\2\u008a"+
		"\u008c\7H\2\2\u008b\u0087\3\2\2\2\u008b\u0089\3\2\2\2\u008c\n\3\2\2\2"+
		"\u008d\u008e\7k\2\2\u008e\u0092\7p\2\2\u008f\u0090\7K\2\2\u0090\u0092"+
		"\7P\2\2\u0091\u008d\3\2\2\2\u0091\u008f\3\2\2\2\u0092\f\3\2\2\2\u0093"+
		"\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096\7j\2\2\u0096\u0097\7g\2\2"+
		"\u0097\u0098\7t\2\2\u0098\u0099\7k\2\2\u0099\u009a\7v\2\2\u009a\u00a4"+
		"\7u\2\2\u009b\u009c\7K\2\2\u009c\u009d\7P\2\2\u009d\u009e\7J\2\2\u009e"+
		"\u009f\7G\2\2\u009f\u00a0\7T\2\2\u00a0\u00a1\7K\2\2\u00a1\u00a2\7V\2\2"+
		"\u00a2\u00a4\7U\2\2\u00a3\u0093\3\2\2\2\u00a3\u009b\3\2\2\2\u00a4\16\3"+
		"\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7x\2\2\u00a8"+
		"\u00a9\7q\2\2\u00a9\u00aa\7k\2\2\u00aa\u00b2\7f\2\2\u00ab\u00ac\7K\2\2"+
		"\u00ac\u00ad\7U\2\2\u00ad\u00ae\7X\2\2\u00ae\u00af\7Q\2\2\u00af\u00b0"+
		"\7K\2\2\u00b0\u00b2\7F\2\2\u00b1\u00a5\3\2\2\2\u00b1\u00ab\3\2\2\2\u00b2"+
		"\20\3\2\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7q\2\2\u00b6"+
		"\u00bc\7r\2\2\u00b7\u00b8\7N\2\2\u00b8\u00b9\7Q\2\2\u00b9\u00ba\7Q\2\2"+
		"\u00ba\u00bc\7R\2\2\u00bb\u00b3\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bc\22\3"+
		"\2\2\2\u00bd\u00be\7r\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7q\2\2\u00c0"+
		"\u00c6\7n\2\2\u00c1\u00c2\7R\2\2\u00c2\u00c3\7Q\2\2\u00c3\u00c4\7Q\2\2"+
		"\u00c4\u00c6\7N\2\2\u00c5\u00bd\3\2\2\2\u00c5\u00c1\3\2\2\2\u00c6\24\3"+
		"\2\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7j\2\2\u00c9\u00ca\7g\2\2\u00ca"+
		"\u00d0\7p\2\2\u00cb\u00cc\7V\2\2\u00cc\u00cd\7J\2\2\u00cd\u00ce\7G\2\2"+
		"\u00ce\u00d0\7P\2\2\u00cf\u00c7\3\2\2\2\u00cf\u00cb\3\2\2\2\u00d0\26\3"+
		"\2\2\2\u00d1\u00d2\7y\2\2\u00d2\u00d3\7j\2\2\u00d3\u00d4\7k\2\2\u00d4"+
		"\u00d5\7n\2\2\u00d5\u00dc\7g\2\2\u00d6\u00d7\7Y\2\2\u00d7\u00d8\7J\2\2"+
		"\u00d8\u00d9\7K\2\2\u00d9\u00da\7N\2\2\u00da\u00dc\7G\2\2\u00db\u00d1"+
		"\3\2\2\2\u00db\u00d6\3\2\2\2\u00dc\30\3\2\2\2\u00dd\u00de\7p\2\2\u00de"+
		"\u00df\7g\2\2\u00df\u00e4\7y\2\2\u00e0\u00e1\7P\2\2\u00e1\u00e2\7G\2\2"+
		"\u00e2\u00e4\7Y\2\2\u00e3\u00dd\3\2\2\2\u00e3\u00e0\3\2\2\2\u00e4\32\3"+
		"\2\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7q\2\2\u00e7\u00ec\7v\2\2\u00e8"+
		"\u00e9\7P\2\2\u00e9\u00ea\7Q\2\2\u00ea\u00ec\7V\2\2\u00eb\u00e5\3\2\2"+
		"\2\u00eb\u00e8\3\2\2\2\u00ec\34\3\2\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef"+
		"\7g\2\2\u00ef\u00f4\7v\2\2\u00f0\u00f1\7N\2\2\u00f1\u00f2\7G\2\2\u00f2"+
		"\u00f4\7V\2\2\u00f3\u00ed\3\2\2\2\u00f3\u00f0\3\2\2\2\u00f4\36\3\2\2\2"+
		"\u00f5\u00f6\7h\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9"+
		"\7u\2\2\u00f9\u00fa\7g\2\2\u00fa \3\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd"+
		"\7t\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff\"\3\2\2\2\u0100\u0101"+
		"\7=\2\2\u0101$\3\2\2\2\u0102\u0103\7}\2\2\u0103&\3\2\2\2\u0104\u0105\7"+
		"\177\2\2\u0105(\3\2\2\2\u0106\u0107\7]\2\2\u0107*\3\2\2\2\u0108\u0109"+
		"\7_\2\2\u0109,\3\2\2\2\u010a\u010b\7*\2\2\u010b.\3\2\2\2\u010c\u010d\7"+
		"+\2\2\u010d\60\3\2\2\2\u010e\u010f\7.\2\2\u010f\62\3\2\2\2\u0110\u0111"+
		"\7\60\2\2\u0111\64\3\2\2\2\u0112\u0113\7$\2\2\u0113\66\3\2\2\2\u0114\u0115"+
		"\7)\2\2\u01158\3\2\2\2\u0116\u0117\7-\2\2\u0117:\3\2\2\2\u0118\u0119\7"+
		"/\2\2\u0119<\3\2\2\2\u011a\u011b\7,\2\2\u011b>\3\2\2\2\u011c\u011d\7\61"+
		"\2\2\u011d@\3\2\2\2\u011e\u011f\7\u0080\2\2\u011fB\3\2\2\2\u0120\u0121"+
		"\7<\2\2\u0121D\3\2\2\2\u0122\u0123\7>\2\2\u0123\u0124\7/\2\2\u0124F\3"+
		"\2\2\2\u0125\u0126\7B\2\2\u0126H\3\2\2\2\u0127\u0128\7>\2\2\u0128J\3\2"+
		"\2\2\u0129\u012a\7>\2\2\u012a\u012b\7?\2\2\u012bL\3\2\2\2\u012c\u012d"+
		"\7?\2\2\u012dN\3\2\2\2\u012e\u012f\7/\2\2\u012f\u0130\7/\2\2\u0130\u0134"+
		"\3\2\2\2\u0131\u0133\13\2\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2"+
		"\u0134\u0135\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0137\3\2\2\2\u0136\u0134"+
		"\3\2\2\2\u0137\u0138\7\f\2\2\u0138\u0139\3\2\2\2\u0139\u013a\b(\2\2\u013a"+
		"P\3\2\2\2\u013b\u013c\7*\2\2\u013c\u013d\7,\2\2\u013d\u0141\3\2\2\2\u013e"+
		"\u0140\13\2\2\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u0142\3"+
		"\2\2\2\u0141\u013f\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u0141\3\2\2\2\u0144"+
		"\u0145\7,\2\2\u0145\u0146\7+\2\2\u0146\u0147\3\2\2\2\u0147\u0148\b)\2"+
		"\2\u0148R\3\2\2\2\u0149\u014b\5g\64\2\u014a\u0149\3\2\2\2\u014b\u014c"+
		"\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014dT\3\2\2\2\u014e"+
		"\u0152\7$\2\2\u014f\u0151\n\2\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2"+
		"\2\2\u0152\u0153\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0155\3\2\2\2\u0154"+
		"\u0152\3\2\2\2\u0155\u0156\7$\2\2\u0156V\3\2\2\2\u0157\u015c\5c\62\2\u0158"+
		"\u015b\5_\60\2\u0159\u015b\7a\2\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2"+
		"\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d"+
		"\u0161\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0161\5]/\2\u0160\u0157\3\2\2"+
		"\2\u0160\u015f\3\2\2\2\u0161X\3\2\2\2\u0162\u0167\5e\63\2\u0163\u0166"+
		"\5_\60\2\u0164\u0166\7a\2\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166"+
		"\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016c\3\2"+
		"\2\2\u0169\u0167\3\2\2\2\u016a\u016c\5[.\2\u016b\u0162\3\2\2\2\u016b\u016a"+
		"\3\2\2\2\u016cZ\3\2\2\2\u016d\u016e\7u\2\2\u016e\u016f\7g\2\2\u016f\u0170"+
		"\7n\2\2\u0170\u0171\7h\2\2\u0171\\\3\2\2\2\u0172\u0173\7U\2\2\u0173\u0174"+
		"\7G\2\2\u0174\u0175\7N\2\2\u0175\u0176\7H\2\2\u0176\u0177\7a\2\2\u0177"+
		"\u0178\7V\2\2\u0178\u0179\7[\2\2\u0179\u017a\7R\2\2\u017a\u017b\7G\2\2"+
		"\u017b^\3\2\2\2\u017c\u017f\5a\61\2\u017d\u017f\5g\64\2\u017e\u017c\3"+
		"\2\2\2\u017e\u017d\3\2\2\2\u017f`\3\2\2\2\u0180\u0183\5c\62\2\u0181\u0183"+
		"\5e\63\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183b\3\2\2\2\u0184"+
		"\u0185\4C\\\2\u0185d\3\2\2\2\u0186\u0187\4c|\2\u0187f\3\2\2\2\u0188\u0189"+
		"\t\3\2\2\u0189h\3\2\2\2\u018a\u018c\t\4\2\2\u018b\u018a\3\2\2\2\u018c"+
		"\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2"+
		"\2\2\u018f\u0190\b\65\2\2\u0190j\3\2\2\2\36\2u\177\u0085\u008b\u0091\u00a3"+
		"\u00b1\u00bb\u00c5\u00cf\u00db\u00e3\u00eb\u00f3\u0134\u0141\u014c\u0152"+
		"\u015a\u015c\u0160\u0165\u0167\u016b\u017e\u0182\u018d\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
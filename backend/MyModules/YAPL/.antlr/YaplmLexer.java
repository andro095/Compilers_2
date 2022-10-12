// Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/backend/MyModules/YAPL/Yaplo.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YaplmLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, ELSE=2, FI=3, IF=4, IN=5, INHERITS=6, ISVOID=7, LOOP=8, POOL=9, 
		THEN=10, WHILE=11, NEW=12, NOT=13, LET=14, FALSE=15, TRUE=16, VOID=17, 
		SEMICOLON=18, LCURLY=19, RCURLY=20, LSQUARE=21, RSQUARE=22, LROUND=23, 
		RROUND=24, COMMA=25, POINT=26, QUOTES=27, APOSTROPHE=28, ADD=29, SUB=30, 
		MULTIPLY=31, DIVIDE=32, INT_NOT=33, COLON=34, ASIGN=35, ARROBA=36, LESS_THAN=37, 
		LESS_EQUAL=38, EQUAL=39, LINE_COMMENT=40, COMMENT=41, INTEGER=42, STRING=43, 
		TYPE=44, ID=45, WS=46, ERR_TOKEN=47;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", "POOL", 
			"THEN", "WHILE", "NEW", "NOT", "LET", "FALSE", "TRUE", "VOID", "SEMICOLON", 
			"LCURLY", "RCURLY", "LSQUARE", "RSQUARE", "LROUND", "RROUND", "COMMA", 
			"POINT", "QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", "DIVIDE", 
			"INT_NOT", "COLON", "ASIGN", "ARROBA", "LESS_THAN", "LESS_EQUAL", "EQUAL", 
			"LINE_COMMENT", "COMMENT", "INTEGER", "STRING", "TYPE", "ID", "SELF", 
			"SELF_TYPE", "LETTER_NUM", "LETTER", "MAYUS", "MINUS", "DIGIT", "WS", 
			"ERR_TOKEN"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "'false'", "'true'", "'void'", "';'", "'{'", "'}'", 
			"'['", "']'", "'('", "')'", "','", "'.'", "'\"'", "'''", "'+'", "'-'", 
			"'*'", "'/'", "'~'", "':'", "'<-'", "'@'", "'<'", "'<='", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", 
			"POOL", "THEN", "WHILE", "NEW", "NOT", "LET", "FALSE", "TRUE", "VOID", 
			"SEMICOLON", "LCURLY", "RCURLY", "LSQUARE", "RSQUARE", "LROUND", "RROUND", 
			"COMMA", "POINT", "QUOTES", "APOSTROPHE", "ADD", "SUB", "MULTIPLY", "DIVIDE", 
			"INT_NOT", "COLON", "ASIGN", "ARROBA", "LESS_THAN", "LESS_EQUAL", "EQUAL", 
			"LINE_COMMENT", "COMMENT", "INTEGER", "STRING", "TYPE", "ID", "WS", "ERR_TOKEN"
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


	public YaplmLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Yaplo.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61\u019e\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\5\2z\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0084\n\3\3\4\3\4"+
		"\3\4\3\4\5\4\u008a\n\4\3\5\3\5\3\5\3\5\5\5\u0090\n\5\3\6\3\6\3\6\3\6\5"+
		"\6\u0096\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\5\7\u00a8\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5"+
		"\b\u00b6\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00c0\n\t\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\5\n\u00ca\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\5\13\u00d4\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00e0"+
		"\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e8\n\r\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\5\16\u00f0\n\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00f8\n\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22"+
		"\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31"+
		"\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3"+
		" \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)"+
		"\3)\7)\u013c\n)\f)\16)\u013f\13)\3)\3)\3)\3)\3*\3*\3*\3*\7*\u0149\n*\f"+
		"*\16*\u014c\13*\3*\3*\3*\3*\3*\3+\6+\u0154\n+\r+\16+\u0155\3,\3,\3,\3"+
		",\7,\u015c\n,\f,\16,\u015f\13,\3,\3,\3-\3-\3-\7-\u0166\n-\f-\16-\u0169"+
		"\13-\3-\5-\u016c\n-\3.\3.\3.\7.\u0171\n.\f.\16.\u0174\13.\3.\5.\u0177"+
		"\n.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3"+
		"\61\3\61\5\61\u018a\n\61\3\62\3\62\5\62\u018e\n\62\3\63\3\63\3\64\3\64"+
		"\3\65\3\65\3\66\6\66\u0197\n\66\r\66\16\66\u0198\3\66\3\66\3\67\3\67\4"+
		"\u013d\u014a\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31"+
		"\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65"+
		"\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2c\2e\2g\2"+
		"i\2k\60m\61\3\2\6\b\2$$))^^ddhhvv\6\2\f\f\17\17$$^^\3\2\62;\5\2\n\f\16"+
		"\17\"\"\2\u01b2\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3"+
		"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2"+
		"\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2"+
		"9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3"+
		"\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2"+
		"\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2k\3\2\2\2\2"+
		"m\3\2\2\2\3y\3\2\2\2\5\u0083\3\2\2\2\7\u0089\3\2\2\2\t\u008f\3\2\2\2\13"+
		"\u0095\3\2\2\2\r\u00a7\3\2\2\2\17\u00b5\3\2\2\2\21\u00bf\3\2\2\2\23\u00c9"+
		"\3\2\2\2\25\u00d3\3\2\2\2\27\u00df\3\2\2\2\31\u00e7\3\2\2\2\33\u00ef\3"+
		"\2\2\2\35\u00f7\3\2\2\2\37\u00f9\3\2\2\2!\u00ff\3\2\2\2#\u0104\3\2\2\2"+
		"%\u0109\3\2\2\2\'\u010b\3\2\2\2)\u010d\3\2\2\2+\u010f\3\2\2\2-\u0111\3"+
		"\2\2\2/\u0113\3\2\2\2\61\u0115\3\2\2\2\63\u0117\3\2\2\2\65\u0119\3\2\2"+
		"\2\67\u011b\3\2\2\29\u011d\3\2\2\2;\u011f\3\2\2\2=\u0121\3\2\2\2?\u0123"+
		"\3\2\2\2A\u0125\3\2\2\2C\u0127\3\2\2\2E\u0129\3\2\2\2G\u012b\3\2\2\2I"+
		"\u012e\3\2\2\2K\u0130\3\2\2\2M\u0132\3\2\2\2O\u0135\3\2\2\2Q\u0137\3\2"+
		"\2\2S\u0144\3\2\2\2U\u0153\3\2\2\2W\u0157\3\2\2\2Y\u016b\3\2\2\2[\u0176"+
		"\3\2\2\2]\u0178\3\2\2\2_\u017d\3\2\2\2a\u0189\3\2\2\2c\u018d\3\2\2\2e"+
		"\u018f\3\2\2\2g\u0191\3\2\2\2i\u0193\3\2\2\2k\u0196\3\2\2\2m\u019c\3\2"+
		"\2\2op\7e\2\2pq\7n\2\2qr\7c\2\2rs\7u\2\2sz\7u\2\2tu\7E\2\2uv\7N\2\2vw"+
		"\7C\2\2wx\7U\2\2xz\7U\2\2yo\3\2\2\2yt\3\2\2\2z\4\3\2\2\2{|\7g\2\2|}\7"+
		"n\2\2}~\7u\2\2~\u0084\7g\2\2\177\u0080\7G\2\2\u0080\u0081\7N\2\2\u0081"+
		"\u0082\7U\2\2\u0082\u0084\7G\2\2\u0083{\3\2\2\2\u0083\177\3\2\2\2\u0084"+
		"\6\3\2\2\2\u0085\u0086\7h\2\2\u0086\u008a\7k\2\2\u0087\u0088\7H\2\2\u0088"+
		"\u008a\7K\2\2\u0089\u0085\3\2\2\2\u0089\u0087\3\2\2\2\u008a\b\3\2\2\2"+
		"\u008b\u008c\7k\2\2\u008c\u0090\7h\2\2\u008d\u008e\7K\2\2\u008e\u0090"+
		"\7H\2\2\u008f\u008b\3\2\2\2\u008f\u008d\3\2\2\2\u0090\n\3\2\2\2\u0091"+
		"\u0092\7k\2\2\u0092\u0096\7p\2\2\u0093\u0094\7K\2\2\u0094\u0096\7P\2\2"+
		"\u0095\u0091\3\2\2\2\u0095\u0093\3\2\2\2\u0096\f\3\2\2\2\u0097\u0098\7"+
		"k\2\2\u0098\u0099\7p\2\2\u0099\u009a\7j\2\2\u009a\u009b\7g\2\2\u009b\u009c"+
		"\7t\2\2\u009c\u009d\7k\2\2\u009d\u009e\7v\2\2\u009e\u00a8\7u\2\2\u009f"+
		"\u00a0\7K\2\2\u00a0\u00a1\7P\2\2\u00a1\u00a2\7J\2\2\u00a2\u00a3\7G\2\2"+
		"\u00a3\u00a4\7T\2\2\u00a4\u00a5\7K\2\2\u00a5\u00a6\7V\2\2\u00a6\u00a8"+
		"\7U\2\2\u00a7\u0097\3\2\2\2\u00a7\u009f\3\2\2\2\u00a8\16\3\2\2\2\u00a9"+
		"\u00aa\7k\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7x\2\2\u00ac\u00ad\7q\2\2"+
		"\u00ad\u00ae\7k\2\2\u00ae\u00b6\7f\2\2\u00af\u00b0\7K\2\2\u00b0\u00b1"+
		"\7U\2\2\u00b1\u00b2\7X\2\2\u00b2\u00b3\7Q\2\2\u00b3\u00b4\7K\2\2\u00b4"+
		"\u00b6\7F\2\2\u00b5\u00a9\3\2\2\2\u00b5\u00af\3\2\2\2\u00b6\20\3\2\2\2"+
		"\u00b7\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7q\2\2\u00ba\u00c0"+
		"\7r\2\2\u00bb\u00bc\7N\2\2\u00bc\u00bd\7Q\2\2\u00bd\u00be\7Q\2\2\u00be"+
		"\u00c0\7R\2\2\u00bf\u00b7\3\2\2\2\u00bf\u00bb\3\2\2\2\u00c0\22\3\2\2\2"+
		"\u00c1\u00c2\7r\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7q\2\2\u00c4\u00ca"+
		"\7n\2\2\u00c5\u00c6\7R\2\2\u00c6\u00c7\7Q\2\2\u00c7\u00c8\7Q\2\2\u00c8"+
		"\u00ca\7N\2\2\u00c9\u00c1\3\2\2\2\u00c9\u00c5\3\2\2\2\u00ca\24\3\2\2\2"+
		"\u00cb\u00cc\7v\2\2\u00cc\u00cd\7j\2\2\u00cd\u00ce\7g\2\2\u00ce\u00d4"+
		"\7p\2\2\u00cf\u00d0\7V\2\2\u00d0\u00d1\7J\2\2\u00d1\u00d2\7G\2\2\u00d2"+
		"\u00d4\7P\2\2\u00d3\u00cb\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d4\26\3\2\2\2"+
		"\u00d5\u00d6\7y\2\2\u00d6\u00d7\7j\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9"+
		"\7n\2\2\u00d9\u00e0\7g\2\2\u00da\u00db\7Y\2\2\u00db\u00dc\7J\2\2\u00dc"+
		"\u00dd\7K\2\2\u00dd\u00de\7N\2\2\u00de\u00e0\7G\2\2\u00df\u00d5\3\2\2"+
		"\2\u00df\u00da\3\2\2\2\u00e0\30\3\2\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3"+
		"\7g\2\2\u00e3\u00e8\7y\2\2\u00e4\u00e5\7P\2\2\u00e5\u00e6\7G\2\2\u00e6"+
		"\u00e8\7Y\2\2\u00e7\u00e1\3\2\2\2\u00e7\u00e4\3\2\2\2\u00e8\32\3\2\2\2"+
		"\u00e9\u00ea\7p\2\2\u00ea\u00eb\7q\2\2\u00eb\u00f0\7v\2\2\u00ec\u00ed"+
		"\7P\2\2\u00ed\u00ee\7Q\2\2\u00ee\u00f0\7V\2\2\u00ef\u00e9\3\2\2\2\u00ef"+
		"\u00ec\3\2\2\2\u00f0\34\3\2\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7g\2\2"+
		"\u00f3\u00f8\7v\2\2\u00f4\u00f5\7N\2\2\u00f5\u00f6\7G\2\2\u00f6\u00f8"+
		"\7V\2\2\u00f7\u00f1\3\2\2\2\u00f7\u00f4\3\2\2\2\u00f8\36\3\2\2\2\u00f9"+
		"\u00fa\7h\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7u\2\2"+
		"\u00fd\u00fe\7g\2\2\u00fe \3\2\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7t\2"+
		"\2\u0101\u0102\7w\2\2\u0102\u0103\7g\2\2\u0103\"\3\2\2\2\u0104\u0105\7"+
		"x\2\2\u0105\u0106\7q\2\2\u0106\u0107\7k\2\2\u0107\u0108\7f\2\2\u0108$"+
		"\3\2\2\2\u0109\u010a\7=\2\2\u010a&\3\2\2\2\u010b\u010c\7}\2\2\u010c(\3"+
		"\2\2\2\u010d\u010e\7\177\2\2\u010e*\3\2\2\2\u010f\u0110\7]\2\2\u0110,"+
		"\3\2\2\2\u0111\u0112\7_\2\2\u0112.\3\2\2\2\u0113\u0114\7*\2\2\u0114\60"+
		"\3\2\2\2\u0115\u0116\7+\2\2\u0116\62\3\2\2\2\u0117\u0118\7.\2\2\u0118"+
		"\64\3\2\2\2\u0119\u011a\7\60\2\2\u011a\66\3\2\2\2\u011b\u011c\7$\2\2\u011c"+
		"8\3\2\2\2\u011d\u011e\7)\2\2\u011e:\3\2\2\2\u011f\u0120\7-\2\2\u0120<"+
		"\3\2\2\2\u0121\u0122\7/\2\2\u0122>\3\2\2\2\u0123\u0124\7,\2\2\u0124@\3"+
		"\2\2\2\u0125\u0126\7\61\2\2\u0126B\3\2\2\2\u0127\u0128\7\u0080\2\2\u0128"+
		"D\3\2\2\2\u0129\u012a\7<\2\2\u012aF\3\2\2\2\u012b\u012c\7>\2\2\u012c\u012d"+
		"\7/\2\2\u012dH\3\2\2\2\u012e\u012f\7B\2\2\u012fJ\3\2\2\2\u0130\u0131\7"+
		">\2\2\u0131L\3\2\2\2\u0132\u0133\7>\2\2\u0133\u0134\7?\2\2\u0134N\3\2"+
		"\2\2\u0135\u0136\7?\2\2\u0136P\3\2\2\2\u0137\u0138\7/\2\2\u0138\u0139"+
		"\7/\2\2\u0139\u013d\3\2\2\2\u013a\u013c\13\2\2\2\u013b\u013a\3\2\2\2\u013c"+
		"\u013f\3\2\2\2\u013d\u013e\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u0140\3\2"+
		"\2\2\u013f\u013d\3\2\2\2\u0140\u0141\7\f\2\2\u0141\u0142\3\2\2\2\u0142"+
		"\u0143\b)\2\2\u0143R\3\2\2\2\u0144\u0145\7*\2\2\u0145\u0146\7,\2\2\u0146"+
		"\u014a\3\2\2\2\u0147\u0149\13\2\2\2\u0148\u0147\3\2\2\2\u0149\u014c\3"+
		"\2\2\2\u014a\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014d\3\2\2\2\u014c"+
		"\u014a\3\2\2\2\u014d\u014e\7,\2\2\u014e\u014f\7+\2\2\u014f\u0150\3\2\2"+
		"\2\u0150\u0151\b*\2\2\u0151T\3\2\2\2\u0152\u0154\5i\65\2\u0153\u0152\3"+
		"\2\2\2\u0154\u0155\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156"+
		"V\3\2\2\2\u0157\u015d\7$\2\2\u0158\u0159\7^\2\2\u0159\u015c\t\2\2\2\u015a"+
		"\u015c\n\3\2\2\u015b\u0158\3\2\2\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2"+
		"\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\3\2\2\2\u015f"+
		"\u015d\3\2\2\2\u0160\u0161\7$\2\2\u0161X\3\2\2\2\u0162\u0167\5e\63\2\u0163"+
		"\u0166\5a\61\2\u0164\u0166\7a\2\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2"+
		"\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168"+
		"\u016c\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016c\5_\60\2\u016b\u0162\3\2"+
		"\2\2\u016b\u016a\3\2\2\2\u016cZ\3\2\2\2\u016d\u0172\5g\64\2\u016e\u0171"+
		"\5a\61\2\u016f\u0171\7a\2\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171"+
		"\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0177\3\2"+
		"\2\2\u0174\u0172\3\2\2\2\u0175\u0177\5]/\2\u0176\u016d\3\2\2\2\u0176\u0175"+
		"\3\2\2\2\u0177\\\3\2\2\2\u0178\u0179\7u\2\2\u0179\u017a\7g\2\2\u017a\u017b"+
		"\7n\2\2\u017b\u017c\7h\2\2\u017c^\3\2\2\2\u017d\u017e\7U\2\2\u017e\u017f"+
		"\7G\2\2\u017f\u0180\7N\2\2\u0180\u0181\7H\2\2\u0181\u0182\7a\2\2\u0182"+
		"\u0183\7V\2\2\u0183\u0184\7[\2\2\u0184\u0185\7R\2\2\u0185\u0186\7G\2\2"+
		"\u0186`\3\2\2\2\u0187\u018a\5c\62\2\u0188\u018a\5i\65\2\u0189\u0187\3"+
		"\2\2\2\u0189\u0188\3\2\2\2\u018ab\3\2\2\2\u018b\u018e\5e\63\2\u018c\u018e"+
		"\5g\64\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018ed\3\2\2\2\u018f"+
		"\u0190\4C\\\2\u0190f\3\2\2\2\u0191\u0192\4c|\2\u0192h\3\2\2\2\u0193\u0194"+
		"\t\4\2\2\u0194j\3\2\2\2\u0195\u0197\t\5\2\2\u0196\u0195\3\2\2\2\u0197"+
		"\u0198\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\3\2"+
		"\2\2\u019a\u019b\b\66\2\2\u019bl\3\2\2\2\u019c\u019d\13\2\2\2\u019dn\3"+
		"\2\2\2\37\2y\u0083\u0089\u008f\u0095\u00a7\u00b5\u00bf\u00c9\u00d3\u00df"+
		"\u00e7\u00ef\u00f7\u013d\u014a\u0155\u015b\u015d\u0165\u0167\u016b\u0170"+
		"\u0172\u0176\u0189\u018d\u0198\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
// Generated from YAPL/Yapl.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YaplParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

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
	public static final int
		RULE_program = 0, RULE_class = 1, RULE_feature = 2, RULE_formal = 3, RULE_expr = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "class", "feature", "formal", "expr"
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

	@Override
	public String getGrammarFileName() { return "Yapl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YaplParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<ClassContext> class_() {
			return getRuleContexts(ClassContext.class);
		}
		public ClassContext class_(int i) {
			return getRuleContext(ClassContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YaplParser.SEMICOLON, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				class_();
				setState(11);
				match(SEMICOLON);
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(YaplParser.CLASS, 0); }
		public List<TerminalNode> TYPE() { return getTokens(YaplParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YaplParser.TYPE, i);
		}
		public TerminalNode LCURLY() { return getToken(YaplParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(YaplParser.RCURLY, 0); }
		public TerminalNode INHERITS() { return getToken(YaplParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YaplParser.SEMICOLON, i);
		}
		public ClassContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).enterClass(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).exitClass(this);
		}
	}

	public final ClassContext class_() throws RecognitionException {
		ClassContext _localctx = new ClassContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			match(CLASS);
			setState(18);
			match(TYPE);
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(19);
				match(INHERITS);
				setState(20);
				match(TYPE);
				}
			}

			setState(23);
			match(LCURLY);
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(24);
				feature();
				setState(25);
				match(SEMICOLON);
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(32);
			match(RCURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FeatureContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YaplParser.ID, 0); }
		public TerminalNode LROUND() { return getToken(YaplParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(YaplParser.RROUND, 0); }
		public TerminalNode COLON() { return getToken(YaplParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YaplParser.TYPE, 0); }
		public TerminalNode LCURLY() { return getToken(YaplParser.LCURLY, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RCURLY() { return getToken(YaplParser.RCURLY, 0); }
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YaplParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YaplParser.COMMA, i);
		}
		public TerminalNode ASIGN() { return getToken(YaplParser.ASIGN, 0); }
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).enterFeature(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).exitFeature(this);
		}
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_feature);
		int _la;
		try {
			setState(60);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				match(ID);
				setState(35);
				match(LROUND);
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(36);
					formal();
					setState(41);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(37);
						match(COMMA);
						setState(38);
						formal();
						}
						}
						setState(43);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(46);
				match(RROUND);
				setState(47);
				match(COLON);
				setState(48);
				match(TYPE);
				setState(49);
				match(LCURLY);
				setState(50);
				expr(0);
				setState(51);
				match(RCURLY);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				match(ID);
				setState(54);
				match(COLON);
				setState(55);
				match(TYPE);
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASIGN) {
					{
					setState(56);
					match(ASIGN);
					setState(57);
					expr(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YaplParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YaplParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YaplParser.TYPE, 0); }
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).enterFormal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).exitFormal(this);
		}
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(ID);
			setState(63);
			match(COLON);
			setState(64);
			match(TYPE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(YaplParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(YaplParser.ID, i);
		}
		public List<TerminalNode> ASIGN() { return getTokens(YaplParser.ASIGN); }
		public TerminalNode ASIGN(int i) {
			return getToken(YaplParser.ASIGN, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LROUND() { return getToken(YaplParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(YaplParser.RROUND, 0); }
		public List<TerminalNode> COMMA() { return getTokens(YaplParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YaplParser.COMMA, i);
		}
		public TerminalNode IF() { return getToken(YaplParser.IF, 0); }
		public TerminalNode THEN() { return getToken(YaplParser.THEN, 0); }
		public TerminalNode ELSE() { return getToken(YaplParser.ELSE, 0); }
		public TerminalNode FI() { return getToken(YaplParser.FI, 0); }
		public TerminalNode WHILE() { return getToken(YaplParser.WHILE, 0); }
		public TerminalNode LOOP() { return getToken(YaplParser.LOOP, 0); }
		public TerminalNode POOL() { return getToken(YaplParser.POOL, 0); }
		public TerminalNode LCURLY() { return getToken(YaplParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(YaplParser.RCURLY, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(YaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YaplParser.SEMICOLON, i);
		}
		public TerminalNode LET() { return getToken(YaplParser.LET, 0); }
		public List<TerminalNode> COLON() { return getTokens(YaplParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(YaplParser.COLON, i);
		}
		public List<TerminalNode> TYPE() { return getTokens(YaplParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YaplParser.TYPE, i);
		}
		public TerminalNode IN() { return getToken(YaplParser.IN, 0); }
		public TerminalNode NEW() { return getToken(YaplParser.NEW, 0); }
		public TerminalNode ISVOID() { return getToken(YaplParser.ISVOID, 0); }
		public TerminalNode INT_NOT() { return getToken(YaplParser.INT_NOT, 0); }
		public TerminalNode NOT() { return getToken(YaplParser.NOT, 0); }
		public TerminalNode INTEGER() { return getToken(YaplParser.INTEGER, 0); }
		public TerminalNode STRING() { return getToken(YaplParser.STRING, 0); }
		public TerminalNode TRUE() { return getToken(YaplParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(YaplParser.FALSE, 0); }
		public TerminalNode ADD() { return getToken(YaplParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(YaplParser.SUB, 0); }
		public TerminalNode MULTIPLY() { return getToken(YaplParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(YaplParser.DIVIDE, 0); }
		public TerminalNode LESS_THAN() { return getToken(YaplParser.LESS_THAN, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(YaplParser.LESS_EQUAL, 0); }
		public TerminalNode EQUAL() { return getToken(YaplParser.EQUAL, 0); }
		public TerminalNode POINT() { return getToken(YaplParser.POINT, 0); }
		public TerminalNode ARROBA() { return getToken(YaplParser.ARROBA, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YaplListener ) ((YaplListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(67);
				match(ID);
				setState(68);
				match(ASIGN);
				setState(69);
				expr(24);
				}
				break;
			case 2:
				{
				setState(70);
				match(ID);
				setState(71);
				match(LROUND);
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0)) {
					{
					setState(72);
					expr(0);
					setState(77);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(73);
						match(COMMA);
						setState(74);
						expr(0);
						}
						}
						setState(79);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(82);
				match(RROUND);
				}
				break;
			case 3:
				{
				setState(83);
				match(IF);
				setState(84);
				expr(0);
				setState(85);
				match(THEN);
				setState(86);
				expr(0);
				setState(87);
				match(ELSE);
				setState(88);
				expr(0);
				setState(89);
				match(FI);
				}
				break;
			case 4:
				{
				setState(91);
				match(WHILE);
				setState(92);
				expr(0);
				setState(93);
				match(LOOP);
				setState(94);
				expr(0);
				setState(95);
				match(POOL);
				}
				break;
			case 5:
				{
				setState(97);
				match(LCURLY);
				setState(101); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(98);
					expr(0);
					setState(99);
					match(SEMICOLON);
					}
					}
					setState(103); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0) );
				setState(105);
				match(RCURLY);
				}
				break;
			case 6:
				{
				setState(107);
				match(LET);
				setState(108);
				match(ID);
				setState(109);
				match(COLON);
				setState(110);
				match(TYPE);
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASIGN) {
					{
					setState(111);
					match(ASIGN);
					setState(112);
					expr(0);
					}
				}

				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(115);
					match(COMMA);
					setState(116);
					match(ID);
					setState(117);
					match(COLON);
					setState(118);
					match(TYPE);
					setState(121);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==ASIGN) {
						{
						setState(119);
						match(ASIGN);
						setState(120);
						expr(0);
						}
					}

					}
					}
					setState(127);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(128);
				match(IN);
				setState(129);
				expr(18);
				}
				break;
			case 7:
				{
				setState(130);
				match(NEW);
				setState(131);
				match(TYPE);
				}
				break;
			case 8:
				{
				setState(132);
				match(ISVOID);
				setState(133);
				expr(16);
				}
				break;
			case 9:
				{
				setState(134);
				match(INT_NOT);
				setState(135);
				expr(11);
				}
				break;
			case 10:
				{
				setState(136);
				match(NOT);
				setState(137);
				expr(7);
				}
				break;
			case 11:
				{
				setState(138);
				match(LROUND);
				setState(139);
				expr(0);
				setState(140);
				match(RROUND);
				}
				break;
			case 12:
				{
				setState(142);
				match(ID);
				}
				break;
			case 13:
				{
				setState(143);
				match(INTEGER);
				}
				break;
			case 14:
				{
				setState(144);
				match(STRING);
				}
				break;
			case 15:
				{
				setState(145);
				match(TRUE);
				}
				break;
			case 16:
				{
				setState(146);
				match(FALSE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(191);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(189);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(149);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(150);
						match(ADD);
						setState(151);
						expr(16);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(152);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(153);
						match(SUB);
						setState(154);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(155);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(156);
						match(MULTIPLY);
						setState(157);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(158);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(159);
						match(DIVIDE);
						setState(160);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(161);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(162);
						match(LESS_THAN);
						setState(163);
						expr(11);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(164);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(165);
						match(LESS_EQUAL);
						setState(166);
						expr(10);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(167);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(168);
						match(EQUAL);
						setState(169);
						expr(9);
						}
						break;
					case 8:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(170);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(173);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==ARROBA) {
							{
							setState(171);
							match(ARROBA);
							setState(172);
							match(TYPE);
							}
						}

						setState(175);
						match(POINT);
						setState(176);
						match(ID);
						setState(177);
						match(LROUND);
						setState(186);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0)) {
							{
							setState(178);
							expr(0);
							setState(183);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==COMMA) {
								{
								{
								setState(179);
								match(COMMA);
								setState(180);
								expr(0);
								}
								}
								setState(185);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(188);
						match(RROUND);
						}
						break;
					}
					} 
				}
				setState(193);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 10);
		case 5:
			return precpred(_ctx, 9);
		case 6:
			return precpred(_ctx, 8);
		case 7:
			return precpred(_ctx, 23);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001-\u00c3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u000e\b\u0000\u000b\u0000\f"+
		"\u0000\u000f\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u0016\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001"+
		"\u001c\b\u0001\n\u0001\f\u0001\u001f\t\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002(\b"+
		"\u0002\n\u0002\f\u0002+\t\u0002\u0003\u0002-\b\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002;\b"+
		"\u0002\u0003\u0002=\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004L\b\u0004\n\u0004"+
		"\f\u0004O\t\u0004\u0003\u0004Q\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0004\u0004f\b\u0004"+
		"\u000b\u0004\f\u0004g\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004r\b\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004z\b\u0004\u0005\u0004|\b\u0004\n\u0004\f\u0004\u007f\t\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004\u0094\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u00ae\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"\u00b6\b\u0004\n\u0004\f\u0004\u00b9\t\u0004\u0003\u0004\u00bb\b\u0004"+
		"\u0001\u0004\u0005\u0004\u00be\b\u0004\n\u0004\f\u0004\u00c1\t\u0004\u0001"+
		"\u0004\u0000\u0001\b\u0005\u0000\u0002\u0004\u0006\b\u0000\u0000\u00e4"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0002\u0011\u0001\u0000\u0000\u0000\u0004"+
		"<\u0001\u0000\u0000\u0000\u0006>\u0001\u0000\u0000\u0000\b\u0093\u0001"+
		"\u0000\u0000\u0000\n\u000b\u0003\u0002\u0001\u0000\u000b\f\u0005\u0011"+
		"\u0000\u0000\f\u000e\u0001\u0000\u0000\u0000\r\n\u0001\u0000\u0000\u0000"+
		"\u000e\u000f\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000\u0000\u0000\u000f"+
		"\u0010\u0001\u0000\u0000\u0000\u0010\u0001\u0001\u0000\u0000\u0000\u0011"+
		"\u0012\u0005\u0001\u0000\u0000\u0012\u0015\u0005+\u0000\u0000\u0013\u0014"+
		"\u0005\u0006\u0000\u0000\u0014\u0016\u0005+\u0000\u0000\u0015\u0013\u0001"+
		"\u0000\u0000\u0000\u0015\u0016\u0001\u0000\u0000\u0000\u0016\u0017\u0001"+
		"\u0000\u0000\u0000\u0017\u001d\u0005\u0012\u0000\u0000\u0018\u0019\u0003"+
		"\u0004\u0002\u0000\u0019\u001a\u0005\u0011\u0000\u0000\u001a\u001c\u0001"+
		"\u0000\u0000\u0000\u001b\u0018\u0001\u0000\u0000\u0000\u001c\u001f\u0001"+
		"\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001e\u0001"+
		"\u0000\u0000\u0000\u001e \u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000"+
		"\u0000\u0000 !\u0005\u0013\u0000\u0000!\u0003\u0001\u0000\u0000\u0000"+
		"\"#\u0005,\u0000\u0000#,\u0005\u0016\u0000\u0000$)\u0003\u0006\u0003\u0000"+
		"%&\u0005\u0018\u0000\u0000&(\u0003\u0006\u0003\u0000\'%\u0001\u0000\u0000"+
		"\u0000(+\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001\u0000"+
		"\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000,$\u0001"+
		"\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000"+
		"./\u0005\u0017\u0000\u0000/0\u0005!\u0000\u000001\u0005+\u0000\u00001"+
		"2\u0005\u0012\u0000\u000023\u0003\b\u0004\u000034\u0005\u0013\u0000\u0000"+
		"4=\u0001\u0000\u0000\u000056\u0005,\u0000\u000067\u0005!\u0000\u00007"+
		":\u0005+\u0000\u000089\u0005\"\u0000\u00009;\u0003\b\u0004\u0000:8\u0001"+
		"\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;=\u0001\u0000\u0000\u0000"+
		"<\"\u0001\u0000\u0000\u0000<5\u0001\u0000\u0000\u0000=\u0005\u0001\u0000"+
		"\u0000\u0000>?\u0005,\u0000\u0000?@\u0005!\u0000\u0000@A\u0005+\u0000"+
		"\u0000A\u0007\u0001\u0000\u0000\u0000BC\u0006\u0004\uffff\uffff\u0000"+
		"CD\u0005,\u0000\u0000DE\u0005\"\u0000\u0000E\u0094\u0003\b\u0004\u0018"+
		"FG\u0005,\u0000\u0000GP\u0005\u0016\u0000\u0000HM\u0003\b\u0004\u0000"+
		"IJ\u0005\u0018\u0000\u0000JL\u0003\b\u0004\u0000KI\u0001\u0000\u0000\u0000"+
		"LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000"+
		"\u0000NQ\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PH\u0001\u0000"+
		"\u0000\u0000PQ\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000R\u0094"+
		"\u0005\u0017\u0000\u0000ST\u0005\u0004\u0000\u0000TU\u0003\b\u0004\u0000"+
		"UV\u0005\n\u0000\u0000VW\u0003\b\u0004\u0000WX\u0005\u0002\u0000\u0000"+
		"XY\u0003\b\u0004\u0000YZ\u0005\u0003\u0000\u0000Z\u0094\u0001\u0000\u0000"+
		"\u0000[\\\u0005\u000b\u0000\u0000\\]\u0003\b\u0004\u0000]^\u0005\b\u0000"+
		"\u0000^_\u0003\b\u0004\u0000_`\u0005\t\u0000\u0000`\u0094\u0001\u0000"+
		"\u0000\u0000ae\u0005\u0012\u0000\u0000bc\u0003\b\u0004\u0000cd\u0005\u0011"+
		"\u0000\u0000df\u0001\u0000\u0000\u0000eb\u0001\u0000\u0000\u0000fg\u0001"+
		"\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000"+
		"hi\u0001\u0000\u0000\u0000ij\u0005\u0013\u0000\u0000j\u0094\u0001\u0000"+
		"\u0000\u0000kl\u0005\u000e\u0000\u0000lm\u0005,\u0000\u0000mn\u0005!\u0000"+
		"\u0000nq\u0005+\u0000\u0000op\u0005\"\u0000\u0000pr\u0003\b\u0004\u0000"+
		"qo\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000r}\u0001\u0000\u0000"+
		"\u0000st\u0005\u0018\u0000\u0000tu\u0005,\u0000\u0000uv\u0005!\u0000\u0000"+
		"vy\u0005+\u0000\u0000wx\u0005\"\u0000\u0000xz\u0003\b\u0004\u0000yw\u0001"+
		"\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z|\u0001\u0000\u0000\u0000"+
		"{s\u0001\u0000\u0000\u0000|\u007f\u0001\u0000\u0000\u0000}{\u0001\u0000"+
		"\u0000\u0000}~\u0001\u0000\u0000\u0000~\u0080\u0001\u0000\u0000\u0000"+
		"\u007f}\u0001\u0000\u0000\u0000\u0080\u0081\u0005\u0005\u0000\u0000\u0081"+
		"\u0094\u0003\b\u0004\u0012\u0082\u0083\u0005\f\u0000\u0000\u0083\u0094"+
		"\u0005+\u0000\u0000\u0084\u0085\u0005\u0007\u0000\u0000\u0085\u0094\u0003"+
		"\b\u0004\u0010\u0086\u0087\u0005 \u0000\u0000\u0087\u0094\u0003\b\u0004"+
		"\u000b\u0088\u0089\u0005\r\u0000\u0000\u0089\u0094\u0003\b\u0004\u0007"+
		"\u008a\u008b\u0005\u0016\u0000\u0000\u008b\u008c\u0003\b\u0004\u0000\u008c"+
		"\u008d\u0005\u0017\u0000\u0000\u008d\u0094\u0001\u0000\u0000\u0000\u008e"+
		"\u0094\u0005,\u0000\u0000\u008f\u0094\u0005)\u0000\u0000\u0090\u0094\u0005"+
		"*\u0000\u0000\u0091\u0094\u0005\u0010\u0000\u0000\u0092\u0094\u0005\u000f"+
		"\u0000\u0000\u0093B\u0001\u0000\u0000\u0000\u0093F\u0001\u0000\u0000\u0000"+
		"\u0093S\u0001\u0000\u0000\u0000\u0093[\u0001\u0000\u0000\u0000\u0093a"+
		"\u0001\u0000\u0000\u0000\u0093k\u0001\u0000\u0000\u0000\u0093\u0082\u0001"+
		"\u0000\u0000\u0000\u0093\u0084\u0001\u0000\u0000\u0000\u0093\u0086\u0001"+
		"\u0000\u0000\u0000\u0093\u0088\u0001\u0000\u0000\u0000\u0093\u008a\u0001"+
		"\u0000\u0000\u0000\u0093\u008e\u0001\u0000\u0000\u0000\u0093\u008f\u0001"+
		"\u0000\u0000\u0000\u0093\u0090\u0001\u0000\u0000\u0000\u0093\u0091\u0001"+
		"\u0000\u0000\u0000\u0093\u0092\u0001\u0000\u0000\u0000\u0094\u00bf\u0001"+
		"\u0000\u0000\u0000\u0095\u0096\n\u000f\u0000\u0000\u0096\u0097\u0005\u001c"+
		"\u0000\u0000\u0097\u00be\u0003\b\u0004\u0010\u0098\u0099\n\u000e\u0000"+
		"\u0000\u0099\u009a\u0005\u001d\u0000\u0000\u009a\u00be\u0003\b\u0004\u000f"+
		"\u009b\u009c\n\r\u0000\u0000\u009c\u009d\u0005\u001e\u0000\u0000\u009d"+
		"\u00be\u0003\b\u0004\u000e\u009e\u009f\n\f\u0000\u0000\u009f\u00a0\u0005"+
		"\u001f\u0000\u0000\u00a0\u00be\u0003\b\u0004\r\u00a1\u00a2\n\n\u0000\u0000"+
		"\u00a2\u00a3\u0005$\u0000\u0000\u00a3\u00be\u0003\b\u0004\u000b\u00a4"+
		"\u00a5\n\t\u0000\u0000\u00a5\u00a6\u0005%\u0000\u0000\u00a6\u00be\u0003"+
		"\b\u0004\n\u00a7\u00a8\n\b\u0000\u0000\u00a8\u00a9\u0005&\u0000\u0000"+
		"\u00a9\u00be\u0003\b\u0004\t\u00aa\u00ad\n\u0017\u0000\u0000\u00ab\u00ac"+
		"\u0005#\u0000\u0000\u00ac\u00ae\u0005+\u0000\u0000\u00ad\u00ab\u0001\u0000"+
		"\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae\u00af\u0001\u0000"+
		"\u0000\u0000\u00af\u00b0\u0005\u0019\u0000\u0000\u00b0\u00b1\u0005,\u0000"+
		"\u0000\u00b1\u00ba\u0005\u0016\u0000\u0000\u00b2\u00b7\u0003\b\u0004\u0000"+
		"\u00b3\u00b4\u0005\u0018\u0000\u0000\u00b4\u00b6\u0003\b\u0004\u0000\u00b5"+
		"\u00b3\u0001\u0000\u0000\u0000\u00b6\u00b9\u0001\u0000\u0000\u0000\u00b7"+
		"\u00b5\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8"+
		"\u00bb\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00ba"+
		"\u00b2\u0001\u0000\u0000\u0000\u00ba\u00bb\u0001\u0000\u0000\u0000\u00bb"+
		"\u00bc\u0001\u0000\u0000\u0000\u00bc\u00be\u0005\u0017\u0000\u0000\u00bd"+
		"\u0095\u0001\u0000\u0000\u0000\u00bd\u0098\u0001\u0000\u0000\u0000\u00bd"+
		"\u009b\u0001\u0000\u0000\u0000\u00bd\u009e\u0001\u0000\u0000\u0000\u00bd"+
		"\u00a1\u0001\u0000\u0000\u0000\u00bd\u00a4\u0001\u0000\u0000\u0000\u00bd"+
		"\u00a7\u0001\u0000\u0000\u0000\u00bd\u00aa\u0001\u0000\u0000\u0000\u00be"+
		"\u00c1\u0001\u0000\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00bf"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c0\t\u0001\u0000\u0000\u0000\u00c1\u00bf"+
		"\u0001\u0000\u0000\u0000\u0013\u000f\u0015\u001d),:<MPgqy}\u0093\u00ad"+
		"\u00b7\u00ba\u00bd\u00bf";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
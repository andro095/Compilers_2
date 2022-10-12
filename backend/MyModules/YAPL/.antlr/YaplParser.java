// Generated from /Users/andrerodriguez/Documents/Github/University/Compilers_2/backend/MyModules/YAPL/Yapl.g4 by ANTLR 4.9.2
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
		public List<ClassContext> class() {
			return getRuleContexts(ClassContext.class);
		}
		public ClassContext class(int i) {
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
				class();
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
	}

	public final ClassContext class() throws RecognitionException {
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
		public TerminalNode LROUND() { return getToken(YaplParser.LROUND, 0); }
		public TerminalNode RROUND() { return getToken(YaplParser.RROUND, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
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
		public TerminalNode NEW() { return getToken(YaplParser.NEW, 0); }
		public List<TerminalNode> TYPE() { return getTokens(YaplParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YaplParser.TYPE, i);
		}
		public TerminalNode INT_NOT() { return getToken(YaplParser.INT_NOT, 0); }
		public TerminalNode ISVOID() { return getToken(YaplParser.ISVOID, 0); }
		public TerminalNode NOT() { return getToken(YaplParser.NOT, 0); }
		public TerminalNode LET() { return getToken(YaplParser.LET, 0); }
		public List<TerminalNode> COLON() { return getTokens(YaplParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(YaplParser.COLON, i);
		}
		public TerminalNode IN() { return getToken(YaplParser.IN, 0); }
		public List<TerminalNode> ASIGN() { return getTokens(YaplParser.ASIGN); }
		public TerminalNode ASIGN(int i) {
			return getToken(YaplParser.ASIGN, i);
		}
		public TerminalNode INTEGER() { return getToken(YaplParser.INTEGER, 0); }
		public TerminalNode STRING() { return getToken(YaplParser.STRING, 0); }
		public TerminalNode TRUE() { return getToken(YaplParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(YaplParser.FALSE, 0); }
		public TerminalNode MULTIPLY() { return getToken(YaplParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(YaplParser.DIVIDE, 0); }
		public TerminalNode ADD() { return getToken(YaplParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(YaplParser.SUB, 0); }
		public TerminalNode LESS_THAN() { return getToken(YaplParser.LESS_THAN, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(YaplParser.LESS_EQUAL, 0); }
		public TerminalNode EQUAL() { return getToken(YaplParser.EQUAL, 0); }
		public TerminalNode POINT() { return getToken(YaplParser.POINT, 0); }
		public TerminalNode ARROBA() { return getToken(YaplParser.ARROBA, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
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
				match(LROUND);
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0)) {
					{
					setState(69);
					expr(0);
					setState(74);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(70);
						match(COMMA);
						setState(71);
						expr(0);
						}
						}
						setState(76);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(79);
				match(RROUND);
				}
				break;
			case 2:
				{
				setState(80);
				match(IF);
				setState(81);
				expr(0);
				setState(82);
				match(THEN);
				setState(83);
				expr(0);
				setState(84);
				match(ELSE);
				setState(85);
				expr(0);
				setState(86);
				match(FI);
				}
				break;
			case 3:
				{
				setState(88);
				match(WHILE);
				setState(89);
				expr(0);
				setState(90);
				match(LOOP);
				setState(91);
				expr(0);
				setState(92);
				match(POOL);
				}
				break;
			case 4:
				{
				setState(94);
				match(LCURLY);
				setState(98); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(95);
					expr(0);
					setState(96);
					match(SEMICOLON);
					}
					}
					setState(100); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0) );
				setState(102);
				match(RCURLY);
				}
				break;
			case 5:
				{
				setState(104);
				match(NEW);
				setState(105);
				match(TYPE);
				}
				break;
			case 6:
				{
				setState(106);
				match(LROUND);
				setState(107);
				expr(0);
				setState(108);
				match(RROUND);
				}
				break;
			case 7:
				{
				setState(110);
				match(INT_NOT);
				setState(111);
				expr(13);
				}
				break;
			case 8:
				{
				setState(112);
				match(ISVOID);
				setState(113);
				expr(12);
				}
				break;
			case 9:
				{
				setState(114);
				match(NOT);
				setState(115);
				expr(8);
				}
				break;
			case 10:
				{
				setState(116);
				match(LET);
				setState(117);
				match(ID);
				setState(118);
				match(COLON);
				setState(119);
				match(TYPE);
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASIGN) {
					{
					setState(120);
					match(ASIGN);
					setState(121);
					expr(0);
					}
				}

				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(124);
					match(COMMA);
					setState(125);
					match(ID);
					setState(126);
					match(COLON);
					setState(127);
					match(TYPE);
					setState(130);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==ASIGN) {
						{
						setState(128);
						match(ASIGN);
						setState(129);
						expr(0);
						}
					}

					}
					}
					setState(136);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(137);
				match(IN);
				setState(138);
				expr(7);
				}
				break;
			case 11:
				{
				setState(139);
				match(ID);
				setState(140);
				match(ASIGN);
				setState(141);
				expr(6);
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
			setState(179);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(177);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(149);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(150);
						_la = _input.LA(1);
						if ( !(_la==MULTIPLY || _la==DIVIDE) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(151);
						expr(12);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(152);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(153);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(154);
						expr(11);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(155);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(156);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS_THAN) | (1L << LESS_EQUAL) | (1L << EQUAL))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(157);
						expr(10);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(158);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(161);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==ARROBA) {
							{
							setState(159);
							match(ARROBA);
							setState(160);
							match(TYPE);
							}
						}

						setState(163);
						match(POINT);
						setState(164);
						match(ID);
						setState(165);
						match(LROUND);
						setState(174);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << LET) | (1L << FALSE) | (1L << TRUE) | (1L << LCURLY) | (1L << LROUND) | (1L << INT_NOT) | (1L << INTEGER) | (1L << STRING) | (1L << ID))) != 0)) {
							{
							setState(166);
							expr(0);
							setState(171);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==COMMA) {
								{
								{
								setState(167);
								match(COMMA);
								setState(168);
								expr(0);
								}
								}
								setState(173);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(176);
						match(RROUND);
						}
						break;
					}
					} 
				}
				setState(181);
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
			return precpred(_ctx, 11);
		case 1:
			return precpred(_ctx, 10);
		case 2:
			return precpred(_ctx, 9);
		case 3:
			return precpred(_ctx, 20);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61\u00b9\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\6\2\20\n\2\r\2\16\2\21\3"+
		"\3\3\3\3\3\3\3\5\3\30\n\3\3\3\3\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3"+
		"\3\3\3\3\4\3\4\3\4\3\4\3\4\7\4*\n\4\f\4\16\4-\13\4\5\4/\n\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\5\4?\n\4\3\5\3\5\3\5\3"+
		"\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6K\n\6\f\6\16\6N\13\6\5\6P\n\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\6\6"+
		"e\n\6\r\6\16\6f\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6}\n\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0085"+
		"\n\6\7\6\u0087\n\6\f\6\16\6\u008a\13\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\5\6\u0096\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\5\6\u00a4\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00ac\n\6\f\6\16\6\u00af\13"+
		"\6\5\6\u00b1\n\6\3\6\7\6\u00b4\n\6\f\6\16\6\u00b7\13\6\3\6\2\3\n\7\2\4"+
		"\6\b\n\2\5\3\2!\"\3\2\37 \3\2\')\2\u00d6\2\17\3\2\2\2\4\23\3\2\2\2\6>"+
		"\3\2\2\2\b@\3\2\2\2\n\u0095\3\2\2\2\f\r\5\4\3\2\r\16\7\24\2\2\16\20\3"+
		"\2\2\2\17\f\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2"+
		"\2\2\23\24\7\3\2\2\24\27\7.\2\2\25\26\7\b\2\2\26\30\7.\2\2\27\25\3\2\2"+
		"\2\27\30\3\2\2\2\30\31\3\2\2\2\31\37\7\25\2\2\32\33\5\6\4\2\33\34\7\24"+
		"\2\2\34\36\3\2\2\2\35\32\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2"+
		" \"\3\2\2\2!\37\3\2\2\2\"#\7\26\2\2#\5\3\2\2\2$%\7/\2\2%.\7\31\2\2&+\5"+
		"\b\5\2\'(\7\33\2\2(*\5\b\5\2)\'\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2"+
		",/\3\2\2\2-+\3\2\2\2.&\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\7\32\2\2\61"+
		"\62\7$\2\2\62\63\7.\2\2\63\64\7\25\2\2\64\65\5\n\6\2\65\66\7\26\2\2\66"+
		"?\3\2\2\2\678\7/\2\289\7$\2\29<\7.\2\2:;\7%\2\2;=\5\n\6\2<:\3\2\2\2<="+
		"\3\2\2\2=?\3\2\2\2>$\3\2\2\2>\67\3\2\2\2?\7\3\2\2\2@A\7/\2\2AB\7$\2\2"+
		"BC\7.\2\2C\t\3\2\2\2DE\b\6\1\2EF\7/\2\2FO\7\31\2\2GL\5\n\6\2HI\7\33\2"+
		"\2IK\5\n\6\2JH\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MP\3\2\2\2NL\3\2\2"+
		"\2OG\3\2\2\2OP\3\2\2\2PQ\3\2\2\2Q\u0096\7\32\2\2RS\7\6\2\2ST\5\n\6\2T"+
		"U\7\f\2\2UV\5\n\6\2VW\7\4\2\2WX\5\n\6\2XY\7\5\2\2Y\u0096\3\2\2\2Z[\7\r"+
		"\2\2[\\\5\n\6\2\\]\7\n\2\2]^\5\n\6\2^_\7\13\2\2_\u0096\3\2\2\2`d\7\25"+
		"\2\2ab\5\n\6\2bc\7\24\2\2ce\3\2\2\2da\3\2\2\2ef\3\2\2\2fd\3\2\2\2fg\3"+
		"\2\2\2gh\3\2\2\2hi\7\26\2\2i\u0096\3\2\2\2jk\7\16\2\2k\u0096\7.\2\2lm"+
		"\7\31\2\2mn\5\n\6\2no\7\32\2\2o\u0096\3\2\2\2pq\7#\2\2q\u0096\5\n\6\17"+
		"rs\7\t\2\2s\u0096\5\n\6\16tu\7\17\2\2u\u0096\5\n\6\nvw\7\20\2\2wx\7/\2"+
		"\2xy\7$\2\2y|\7.\2\2z{\7%\2\2{}\5\n\6\2|z\3\2\2\2|}\3\2\2\2}\u0088\3\2"+
		"\2\2~\177\7\33\2\2\177\u0080\7/\2\2\u0080\u0081\7$\2\2\u0081\u0084\7."+
		"\2\2\u0082\u0083\7%\2\2\u0083\u0085\5\n\6\2\u0084\u0082\3\2\2\2\u0084"+
		"\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086~\3\2\2\2\u0087\u008a\3\2\2\2"+
		"\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u0088"+
		"\3\2\2\2\u008b\u008c\7\7\2\2\u008c\u0096\5\n\6\t\u008d\u008e\7/\2\2\u008e"+
		"\u008f\7%\2\2\u008f\u0096\5\n\6\b\u0090\u0096\7/\2\2\u0091\u0096\7,\2"+
		"\2\u0092\u0096\7-\2\2\u0093\u0096\7\22\2\2\u0094\u0096\7\21\2\2\u0095"+
		"D\3\2\2\2\u0095R\3\2\2\2\u0095Z\3\2\2\2\u0095`\3\2\2\2\u0095j\3\2\2\2"+
		"\u0095l\3\2\2\2\u0095p\3\2\2\2\u0095r\3\2\2\2\u0095t\3\2\2\2\u0095v\3"+
		"\2\2\2\u0095\u008d\3\2\2\2\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095"+
		"\u0092\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u00b5\3\2"+
		"\2\2\u0097\u0098\f\r\2\2\u0098\u0099\t\2\2\2\u0099\u00b4\5\n\6\16\u009a"+
		"\u009b\f\f\2\2\u009b\u009c\t\3\2\2\u009c\u00b4\5\n\6\r\u009d\u009e\f\13"+
		"\2\2\u009e\u009f\t\4\2\2\u009f\u00b4\5\n\6\f\u00a0\u00a3\f\26\2\2\u00a1"+
		"\u00a2\7&\2\2\u00a2\u00a4\7.\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2"+
		"\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7\34\2\2\u00a6\u00a7\7/\2\2\u00a7\u00b0"+
		"\7\31\2\2\u00a8\u00ad\5\n\6\2\u00a9\u00aa\7\33\2\2\u00aa\u00ac\5\n\6\2"+
		"\u00ab\u00a9\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae"+
		"\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00a8\3\2\2\2\u00b0"+
		"\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\7\32\2\2\u00b3\u0097\3"+
		"\2\2\2\u00b3\u009a\3\2\2\2\u00b3\u009d\3\2\2\2\u00b3\u00a0\3\2\2\2\u00b4"+
		"\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\13\3\2\2"+
		"\2\u00b7\u00b5\3\2\2\2\25\21\27\37+.<>LOf|\u0084\u0088\u0095\u00a3\u00ad"+
		"\u00b0\u00b3\u00b5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
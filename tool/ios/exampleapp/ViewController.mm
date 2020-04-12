#import "ViewController.h"
#import <helloworld/time_repository.h>

@interface ViewController () {
}
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    TimeRepository timeRepository;

    UITextField *textField = [[UITextField alloc] initWithFrame:CGRectMake(10, 200, 300, 40)];
    NSString *currentTime = [NSString stringWithCString:timeRepository.GetCurrentTime().c_str()
                                               encoding:[NSString defaultCStringEncoding]];
    textField.text = [NSString stringWithFormat:@"Current time: %@", currentTime];

    [self.view addSubview:textField];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
